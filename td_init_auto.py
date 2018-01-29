import sys
from pywinauto.application import Application
import pywinauto.timings


print('Argument List:', str(sys.argv))
if len(sys.argv) < 2:
    print('Usage: python tdInitAuto.py "password" ')
else:
    pw = sys.argv[1]
    print("password :", pw)
    app = pywinauto.Application()
    title = u"CybosPlus 주문확인*"
    handle = pywinauto.timings.WaitUntilPasses(20, 0.5, lambda: pywinauto.findwindows.find_window(title_re=title))
    app_con = app.connect(handle=handle)
    window = pywinauto.timings.WaitUntilPasses(20, 0.5, lambda : app_con.window_(title_re=title))
    window.DrawOutline()
    window.SetFocus()
    window.CheckBox.UnCheck()
    window.TypeKeys("%s{ENTER}"%(pw))

