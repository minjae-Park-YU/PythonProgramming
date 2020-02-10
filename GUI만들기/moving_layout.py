import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK") #버튼 만들기
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout() #가로 레이아웃 만들기(왼쪽 밑 -> 오른쪽 밑으로 쌓임)
        hbox.addStretch(1) #버튼을 제외한 남은부분의 공간을 의미하는 함수.
        hbox.addWidget(okButton)  #위의 함수 덕분에 창 크기를 늘려도 빈공간이 같이 늘어나서 오른쪽 밑에 버튼 고정.
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1) #stretch 만듬
        vbox.addLayout(hbox) #아까 만든 버튼 넣기

        self.setLayout(vbox) #그냥 공식처럼 보기. 잘 모르겠음 왜 세로로 하지
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Buttons")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())