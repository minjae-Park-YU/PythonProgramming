import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e): #원래 있는 함수 재정의함.
        if e.key() == Qt.Key_Escape: #A를 누르면 e라는 객체 안에 코드화 된 'A'가 들어감. e.key()하면
            self.close()             #코드 A의 상수를 불러옴. close()하면 창 닫는거임.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())