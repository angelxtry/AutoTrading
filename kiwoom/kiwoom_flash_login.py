import os
import time

from pywinauto import application
from pywinauto import timings

from kiwoom.kiwoom_user_info import UserInfo

app = application.Application()
app.start("C:/Kiwoom/KiwoomFlash3/bin/NKMiniStarter.exe")

title = "번개3 Login"
dlg = timings.WaitUntilPasses(30, 0.5, lambda: app.window_(title=title))

pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys(UserInfo.pw)

cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys(UserInfo.cert)

btn_ctrl = dlg.Button0
btn_ctrl.Click()

time.sleep(50)
os.system("taskkill /im nkmini.exe")
