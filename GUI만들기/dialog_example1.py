import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)  #버튼 추가
        self.btn.move(20, 20)  #위치 변경
        self.btn.clicked.connect(self.showDialog)  #새로 만드는 함수와 연결

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name: ')  #text : Input Dialog, ok : Enter your name으로 할당

        if ok:  #ok가 True인 경우(ok를 누른경우)
            self.le.setText(str(text))  #문자열로 변환해서 값을 넣어줌(setText안에)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())