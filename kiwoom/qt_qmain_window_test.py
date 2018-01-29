import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyStock')
        self.setGeometry(300, 300, 300, 400)

        btn1 = QPushButton('Click me', self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)
        """
        버튼을 클릭하면 clicked 이벤트 발생
        connect 메서드를 사용하여 이벤트와 이벤트를 처리할 메서드를 연결
        """

    def btn1_clicked(self):
        QMessageBox.about(self, 'message', 'clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
