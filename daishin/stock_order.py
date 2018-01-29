import win32com.client
from subprocess import Popen

from daishin import auto_login, connecion
from daishin.order_param import Order, OrderParam
from daishin.request_status import RequestStatus
from daishin.daishin_user_info import UserInfo


def order(buy_sell_flag):
    buy_sell_string = '매수' if buy_sell_flag == Order.buy.value else '매도'

    def inner_func(stock_code, stock_count, price):
        # 주문확인 설정 message box popup
        cp_td_util = win32com.client.Dispatch('CpTrade.CpTdUtil')
        Popen('python td_init_auto.py 1234')
        init_check = cp_td_util.TradeInit(0)
        if init_check != 0:
            print('주문 초기화 실패')
            exit()

        # 주식 매수/매도 주문
        account_number = cp_td_util.AccountNumber[0]  # 계좌번호
        # account_flag = cp_td_util.GoodsList(account_number, 1)  # 주식상품 구분
        # print(account_number, account_flag)  # 10은 무슨 의미?
        cp_td0311 = win32com.client.Dispatch('CpTrade.CpTd0311')
        cp_td0311.SetInputValue(OrderParam.order_type.value, buy_sell_flag)  # 매수/매도
        cp_td0311.SetInputValue(OrderParam.account_number.value, account_number)  # 계좌번호
        cp_td0311.SetInputValue(OrderParam.stock_code.value, stock_code)  # 종목코드
        cp_td0311.SetInputValue(OrderParam.order_count.value, stock_count)  # 매수수량
        cp_td0311.SetInputValue(OrderParam.order_price.value, price)  # 주문단가
        cp_td0311.BlockRequest()

        request_status = cp_td0311.GetDibStatus()
        request_msg = cp_td0311.GetDibMsg1()
        print('Request Status: ', request_status, request_msg)
        if request_status == RequestStatus.success.value:
            print(f'{stock_info.get_code_to_name(stock_code)} {stock_count}주 {price}원 {buy_sell_string} 주문')
        else:
            print(f'{stock_info.get_code_to_name(stock_code)} {buy_sell_string} 주문 Fail.')
            exit()

    return inner_func


def main():
    if connecion.check_connection():
        print('이미 접속 중입니다.')
    else:
        auto_login.execute_cybosplus(UserInfo.id, UserInfo.pw, UserInfo.cert)
    # buy_order = order(Order.buy.value)
    # sell_order = order(Order.sell.value)
    # buy_order('A003540', 10, 17600)


if __name__ == '__main__':
    main()
