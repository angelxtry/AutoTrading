import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyTrader.kiwoom import *

path = os.path.dirname(os.path.abspath(__file__))
form_class = uic.loadUiType(os.path.join(path, 'pytrader.ui'))[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.trade_stocks_done = False

        self.kiwoom = Kiwoom()
        self.kiwoom.comm_connect()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.timer2 = QTimer(self)
        self.timer2.start(1000*10)
        self.timer2.timeout.connect(self.timeout2)

        self.set_account()
        self.stockCodeLineEdit.textChanged.connect(self.code_changed)

        self.orderPushButton.clicked.connect(self.send_order)
        self.lookupPushButton.clicked.connect(self.check_balance)

        self.load_buy_sell_list()

    def timeout(self):
        market_start_time = QTime(9, 0, 0)
        current_time = QTime.currentTime()

        if current_time > market_start_time and\
                self.trade_stocks_done is False:
            self.trade_stocks()
            self.trade_stocks_done = True

        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간: " + text_time

        state = self.kiwoom.get_connect_state()
        if state == 1:
            state_msg = "서버 연결 중"
        else:
            state_msg = "서버 미 연결 중"

        self.statusbar.showMessage(state_msg + " | " + time_msg)

    def timeout2(self):
        if self.realTimeLookupCheckBox.isChecked():
            self.check_balance()

    def code_changed(self):
        code = self.stockCodeLineEdit.text()
        name = self.kiwoom.get_master_code_name(code)
        self.stockNameLineEdit.setText(name)

    def set_account(self):
        cnt = int(self.kiwoom.get_login_info("ACCOUNT_CNT"))
        account_list = self.kiwoom.get_login_info("ACCNO").split(';')
        self.accountComboBox.addItems(account_list[0:cnt])

    def send_order(self):
            order_type_lookup = {'신규매수': 1, '신규매도': 2,
                                 '매수취소': 3, '매도취소': 4}
            hoga_lookup = {'지정가': "00", '시장가': "03"}

            account = self.accountComboBox.currentText()
            order_type = self.orderTypeComboBox.currentText()
            code = self.stockCodeLineEdit.text()
            hoga = self.priceTypeComboBox.currentText()
            num = self.numberSpinBox.value()
            price = self.priceSpinBox.value()

            self.kiwoom.send_order(
                "send_order_req",
                "0101",
                account,
                order_type_lookup[order_type],
                code, num, price, hoga_lookup[hoga], "")

    def check_balance(self):
        self.kiwoom.reset_opw00018_output()
        account_number = self.kiwoom.get_login_info("ACCNO")
        account_number = account_number.split(';')[0]
        # print(account_number)

        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 0, "2000")
        # print(account_number)

        while self.kiwoom.remained_data:
            time.sleep(0.2)
            self.kiwoom.set_input_value("계좌번호", account_number)
            self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 2, "2000")

        # opw00001
        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00001_req", "opw00001", 0, "2000")
        # print(account_number)

        # balance
        item = QTableWidgetItem(self.kiwoom.d2_deposit)
        item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tableWidget.setItem(0, 0, item)

        for i in range(1, 6):
            item = QTableWidgetItem(self.kiwoom.opw00018_output['single'][i - 1])
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
            self.tableWidget.setItem(0, i, item)

        self.tableWidget.resizeRowsToContents()

        # Item list
        item_count = len(self.kiwoom.opw00018_output['multi'])
        self.assetTableWidget.setRowCount(item_count)

        for j in range(item_count):
            row = self.kiwoom.opw00018_output['multi'][j]
            for i in range(len(row)):
                item = QTableWidgetItem(row[i])
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                self.assetTableWidget.setItem(j, i, item)

        self.assetTableWidget.resizeRowsToContents()

    def load_buy_sell_list(self):
        f = open(os.path.join(path, "buy_list.txt"), 'rt')
        buy_list = f.readlines()
        f.close()

        f = open(os.path.join(path, "sell_list.txt"), 'rt')
        sell_list = f.readlines()
        f.close()

        row_count = len(buy_list) + len(sell_list)
        self.sellBuyTableWidget.setRowCount(row_count)

        # buy list
        for j in range(len(buy_list)):
            row_data = buy_list[j]
            split_row_data = row_data.split(';')
            split_row_data[1] = self.kiwoom.get_master_code_name(split_row_data[1].rsplit())

            for i in range(len(split_row_data)):
                item = QTableWidgetItem(split_row_data[i].rstrip())
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                self.sellBuyTableWidget.setItem(j, i, item)

        # sell list
        for j in range(len(sell_list)):
            row_data = sell_list[j]
            split_row_data = row_data.split(';')
            split_row_data[1] = self.kiwoom.get_master_code_name(split_row_data[1].rstrip())

            for i in range(len(split_row_data)):
                item = QTableWidgetItem(split_row_data[i].rstrip())
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                self.sellBuyTableWidget.setItem(len(buy_list) + j, i, item)

        self.sellBuyTableWidget.resizeRowsToContents()

    def trade_stocks(self):
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        f = open(os.path.join(path, "buy_list.txt"), 'rt')
        buy_list = f.readlines()
        f.close()

        f = open(os.path.join(path, "sell_list.txt"), 'rt')
        sell_list = f.readlines()
        f.close()

        # account
        account = self.accountComboBox.currentText()

        # buy list
        for row_data in buy_list:
            split_row_data = row_data.split(';')
            hoga = split_row_data[2]
            code = split_row_data[1]
            num = split_row_data[3]
            price = split_row_data[4]

            if split_row_data[-1].rstrip() == '매수전':
                self.kiwoom.send_order("send_order_req", "0101", account,
                                       1, code, num, price,
                                       hoga_lookup[hoga], "")

        # sell list
        for row_data in sell_list:
            split_row_data = row_data.split(';')
            hoga = split_row_data[2]
            code = split_row_data[1]
            num = split_row_data[3]
            price = split_row_data[4]

            if split_row_data[-1].rstrip() == '매도전':
                self.kiwoom.send_order("send_order_req", "0101", account,
                                       2, code, num, price,
                                       hoga_lookup[hoga], "")

        # buy list
        for i, row_data in enumerate(buy_list):
            buy_list[i] = buy_list[i].replace("매수전", "주문완료")

        # file update
        f = open(os.path.join(path, "buy_list.txt"), 'wt')
        for row_data in buy_list:
            f.write(row_data)
        f.close()

        # sell list
        for i, row_data in enumerate(sell_list):
            sell_list[i] = sell_list[i].replace("매도전", "주문완료")

        # file update
        f = open(os.path.join(path, "sell_list.txt"), 'wt')
        for row_data in sell_list:
            f.write(row_data)
        f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
