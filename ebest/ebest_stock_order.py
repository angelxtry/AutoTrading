import win32com.client
import pythoncom

from ebest.ebest_user_info import UserInfo


class XAQueryEventHandlerCSPAT00600:
    """
    CSPAT00600: 현물 정상 주문
    """
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerCSPAT00600.query_state = 1

    def OnReceiveMessage(self, bool, code, msg):
        XAQueryEventHandlerCSPAT00600.query_state = 1
        print(f'{bool} [{code}]: {msg}')

def order():
    instXAQueryCSPAT00600 = \
        win32com.client.DispatchWithEvents("XA_DataSet.XAQuery",
                                           XAQueryEventHandlerCSPAT00600)

    instXAQueryCSPAT00600.ResFileName = "C:\\eBEST\\xingAPI\\Res\\CSPAT00600.res"
    instXAQueryCSPAT00600.SetFieldData("CSPAT00600InBlock1", "AcntNo", 0, '55501023937')
    instXAQueryCSPAT00600.SetFieldData("CSPAT00600InBlock1", "InptPwd", 0, UserInfo.pw)
    instXAQueryCSPAT00600.SetFieldData("CSPAT00600InBlock1", "IsuNo", 0, 'A078020')
    instXAQueryCSPAT00600.SetFieldData("CSPAT00600InBlock1", "OrdQty", 0, '10')
    instXAQueryCSPAT00600.SetFieldData("CSPAT00600InBlock1", "OrdPrc", 0, '10850')
    instXAQueryCSPAT00600.SetFieldData("CSPAT00600InBlock1", "BnsTpCode", 0, '2')
    instXAQueryCSPAT00600.SetFieldData("CSPAT00600InBlock1", "OrdprcPtnCode", 0, '00')
    instXAQueryCSPAT00600.SetFieldData('CSPAT00600InBlock1', 'MgntrnCode', 0, '000')
    instXAQueryCSPAT00600.SetFieldData('CSPAT00600InBlock1', 'LoanDt', 0, '')
    instXAQueryCSPAT00600.SetFieldData('CSPAT00600InBlock1', 'OrdCndiTpCode', 0, '')
    instXAQueryCSPAT00600.Request(False)

    while XAQueryEventHandlerCSPAT00600.query_state == 0:
        pythoncom.PumpWaitingMessages()

    print(instXAQueryCSPAT00600.GetFieldData('CSPAT00600OutBlock2', 'OrdNo', 0))

if __name__ == '__main__':
    order()
