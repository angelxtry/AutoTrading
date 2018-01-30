import win32com.client
import pythoncom

from ebest.ebest_user_info import UserInfo
from ebest import ebest_login


class XAQueryEventHandlerCSPAQ12300:
    """
    CSPAQ12300: 현물계좌 잔고 내역 조회
    """
    query_state = 0

    # def OnReceiveData(self, code):
    #     XAQueryEventHandlerCSPAT00600.query_state = 1

    def OnReceiveMessage(self, bool, code, msg):
        XAQueryEventHandlerCSPAQ12300.query_state = 1
        print(f'{bool} [{code}]: {msg}')


def get_account_info():
    ebest_login.login()

    instXAQueryCSPAQ12300= \
        win32com.client.DispatchWithEvents("XA_DataSet.XAQuery",
                                           XAQueryEventHandlerCSPAQ12300)

    instXAQueryCSPAQ12300.ResFileName = "C:\\eBEST\\xingAPI\\Res\\CSPAQ12300.res"
    instXAQueryCSPAQ12300.SetFieldData("CSPAQ12300InBlock1", "RecCnt", 0, '00001')
    instXAQueryCSPAQ12300.SetFieldData("CSPAQ12300InBlock1", "AcntNo", 0, '55501023937')
    instXAQueryCSPAQ12300.SetFieldData("CSPAQ12300InBlock1", "Pwd", 0, UserInfo.pw)
    instXAQueryCSPAQ12300.SetFieldData("CSPAQ12300InBlock1", "BalCreTp", 0, '0')
    instXAQueryCSPAQ12300.SetFieldData("CSPAQ12300InBlock1", "CmsnAppTpCode", 0, '0')
    instXAQueryCSPAQ12300.SetFieldData("CSPAQ12300InBlock1", "D2balBaseQryTp", 0, '1')
    instXAQueryCSPAQ12300.SetFieldData("CSPAQ12300InBlock1", "UprcTpCode", 0, '0')
    instXAQueryCSPAQ12300.Request(False)

    while XAQueryEventHandlerCSPAQ12300.query_state == 0:
        pythoncom.PumpWaitingMessages()

    sec_branch_name = instXAQueryCSPAQ12300.GetFieldData('CSPAQ12300OutBlock2', 'BrnNm', 0)
    account_name = instXAQueryCSPAQ12300.GetFieldData('CSPAQ12300OutBlock2', 'AcntNm', 0)
    order_able_cash = instXAQueryCSPAQ12300.GetFieldData('CSPAQ12300OutBlock2', 'MnyOrdAbleAmt', 0)
    withdraw_able_cash = instXAQueryCSPAQ12300.GetFieldData('CSPAQ12300OutBlock2', 'MnyOrdAbleAmt', 0)
    buy_amount = instXAQueryCSPAQ12300.GetFieldData('CSPAQ12300OutBlock2', 'PchsAmt', 0)
    profit_loss_rate = instXAQueryCSPAQ12300.GetFieldData('CSPAQ12300OutBlock2', 'PnlRat', 0)

    print('증권사 지점: ', sec_branch_name)
    print('계좌명: ', account_name)
    print(f'현금주문가능금액: {order_able_cash}')
    print(f'출금가능금액: {withdraw_able_cash}')
    print(f'매입금액: {buy_amount}')
    print(f'손익률: {profit_loss_rate}')


if __name__ == '__main__':
    get_account_info()
