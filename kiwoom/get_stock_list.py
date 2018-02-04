import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *


class Kiwoom(QAxWidget):
    """
    키움증권 OpenAPI+가 제공하는 메서드를 호출하기 위해 QAxWidget 필요
    """
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    """
    com object 생성
    "KHOPENAPI.KHOpenAPICtrl.1"이라는 ProgID를
    QAxWidget 클래스의 생성자로 넘겨주거나 setControl 메서드를 사용
    """
    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)

    """
    로그인, 이벤트 루프 생성
    PyQt를 사용하여 GUI 형태로 만들지 않는다면 명시적으로 이벤트 루프를 생성해야 한다.
    comm_connect() 를 호출하면 로그인 창이 출력됨
    키움증권은 로그인 요청을 받으면 OnEventConnect 이벤트 발생
    이벤트루프를 생성했기 때문에 OnEventConnect 가 발생할 때까지 대기
    """
    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    """
    OnEventConnect 이벤트가 발생하면 _event_connect 메서드가 호출됨
    _set_signal_slots() 에서 설정
    err_code 값에 따라 연결 상태를 출력
    이벤트 루프 종료
    """
    def _event_connect(self, err_code):
        if err_code == 0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market):
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list = code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self, code):
        code_name = self.dynamicCall("GetMasterCodeName(QString)", code)
        return code_name


if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()
    # code_list = kiwoom.get_code_list_by_market('10')
    # [print(code) for code in code_list]
    code_name = kiwoom.get_master_code_name('000660')
    print(code_name)
