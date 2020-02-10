import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0) #컬러 객체 받음(RGB)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)  #프레임 추가
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())  #col(검은색)의 이름을 초기에 씀
        self.frm.setGeometry(130, 22, 100, 100)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()  #색깔 엄청 많은 dialog띄우고 컬러를 특정 개체로 받음

        if col.isValid(): #ok를 누르면 실행
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name()) #선택한 컬러가 들어감.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())