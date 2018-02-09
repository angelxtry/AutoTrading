import sys
import time

from PyQt5.QtWidgets import *

from auto_trading_system.Kiwoom import Kiwoom

app = QApplication(sys.argv)
kiwoom = Kiwoom()
kiwoom.comm_connect()


def get_account_number():
    account_number = kiwoom.get_login_info("ACCNO").split(';')[0]
    # account_number = account_number.split(';')[0]
    print(account_number)
    return account_number


def get_d2deposit(account_number):
    kiwoom.set_input_value("계좌번호", account_number)
    kiwoom.comm_rq_data("opw00001_req", "opw00001", 0, "2000")
    return kiwoom.d2_deposit


def get_balance(account_number):
    kiwoom.reset_opw00018_output()
    kiwoom.set_input_value("계좌번호", account_number)
    kiwoom.comm_rq_data("opw00018_req", "opw00018", 0, "2000")
    while kiwoom.remained_data:
        time.sleep(0.2)
        kiwoom.set_input_value("계좌번호", account_number)
        kiwoom.comm_rq_data("opw00018_req", "opw00018", 2, "2000")
    return kiwoom.opw00018_output


if __name__ == '__main__':
    account_num = get_account_number()
    print(f'예수금: {get_d2deposit(account_num)}')
    dict_balance_info = get_balance(account_num)
    print(dict_balance_info['single'])
    print(dict_balance_info['multi'])
