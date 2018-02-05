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

        self.kiwoom = Kiwoom()
        self.kiwoom.comm_connect()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.set_account()
        self.stockCodeLineEdit.textChanged.connect(self.code_changed)

        self.orderPushButton.clicked.connect(self.send_order)

    def timeout(self):
        current_time = QTime.currentTime()
        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간: " + text_time

        state = self.kiwoom.get_connect_state()
        if state == 1:
            state_msg = "서버 연결 중"
        else:
            state_msg = "서버 미 연결 중"

        self.statusbar.showMessage(state_msg + " | " + time_msg)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
