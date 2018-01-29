import win32com.client
import pythoncom

from ebest import ebest_login


class XAQueryEventHandlerT1102:
    """
    T1102: 주식 현재가(시세) 조회
    """
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT1102.query_state = 1


def get_code_to_name_price(short_code):
    # 078020: 이베스트투자증권
    instXAQueryT1102 = \
        win32com.client.DispatchWithEvents("XA_DataSet.XAQuery",
                                           XAQueryEventHandlerT1102)
    instXAQueryT1102.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1102.res"
    instXAQueryT1102.SetFieldData("t1102InBlock", "shcode", 0, short_code)
    instXAQueryT1102.Request(0)

    while XAQueryEventHandlerT1102.query_state == 0:
        pythoncom.PumpWaitingMessages()

    name = instXAQueryT1102.GetFieldData("t1102OutBlock", "hname", 0)
    price = instXAQueryT1102.GetFieldData("t1102OutBlock", "price", 0)
    print(name)
    print(price)
    return name, price


if __name__ == '__main__':
    ebest_login.login()
    name, price = get_code_to_name_price('078020')
    print(f'종목명: {name}, 현재가 {price}')

