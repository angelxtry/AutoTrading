import time

from pywinauto import application
from pywinauto import timings
import pyautogui


def execute_cybosplus(comm_id="", comm_pw="", cert_pw=""):
    if comm_id == "" or comm_pw == "" or cert_pw == "":
        return None
    app = application.Application().start(r"C:\DAISHIN\STARTER\ncStarter.exe /prj:cp")
    pyautogui.typewrite('\n', interval=0.1)

    try:
        time.sleep(1)
        title = "ncStarter"
        dlg = timings.WaitUntilPasses(2, 0.5, lambda: app.window(title=title))
        btn_ctrl = dlg.Button1
        btn_ctrl.Click()
    except Exception as e:
        print(e)

    try:
        time.sleep(1)
        title = "대신증권 CYBOS FAMILY"
        dlg = timings.WaitUntilPasses(3, 0.5, lambda: app.window(title=title))
        btn_ctrl = dlg.Button1
        btn_ctrl.Click()
    except Exception as e:
        print(e)

    title = "CYBOS Starter"
    main_app = timings.WaitUntilPasses(30, 1, lambda: application.Application().connect(title=title))
    dlg = main_app.window(title=title)

    # print(comm_id, comm_pw, cert_pw)
    mock_invest_btn = dlg.Button11
    mock_invest_btn.Click()
    pass_ctrl = dlg.Edit1
    pass_ctrl.SetFocus()
    pass_ctrl.TypeKeys(comm_id)
    pass_ctrl = dlg.Edit2
    pass_ctrl.SetFocus()
    pass_ctrl.TypeKeys(comm_pw)
    cert_ctrl = dlg.Edit3
    cert_ctrl.SetFocus()
    cert_ctrl.TypeKeys(cert_pw)
    btn_ctrl = dlg.Button
    btn_ctrl.Click()
    time.sleep(5)
    pyautogui.typewrite('\n', interval=0.1)

    return True
