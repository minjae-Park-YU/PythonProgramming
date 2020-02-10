import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self) #가로 슬라이더

        vbox = QVBoxLayout() #세로로 쌓음
        vbox.addWidget(lcd) #LCD먼저 나오고
        vbox.addWidget(sld) #슬라이더 나옴

        self.setLayout(vbox) #전체 창의 레이아웃?
        sld.valueChanged.connect(lcd.display) #슬라이더 값이 변경될 경우, lcd랑 엮어줌

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())