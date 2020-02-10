import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class Communicate(QObject):  #QObject를 상속받아 pyqtSignal()을 사용
    closeApp = pyqtSignal()  #pyqtSignal()은 특정 개체가 신호를 보낼수 있게함. 이제 closeApp이 신호를 보낼수 있음

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close) #창 닫는 함수랑 연결되어있음

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()  #emit() : 신호를 보낼 수 있도록 충격을 주는 역할

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#단계별 설명 : 마우스 클릭(mousePressEvent발생) -> closeAPP객체에서 신호가 방출되면 좋겠음
#             -> closeApp과 연결된 함수(self.close() : 창 꺼지는 함수)
#좀 어려움