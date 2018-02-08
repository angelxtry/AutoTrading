import sys
from PyTrader import pytrader


app = pytrader.QApplication(sys.argv)
myWindow = pytrader.MyWindow()
myWindow.show()
app.exec_()
