import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self) #버튼 만들기
        btn1.move(30, 50) #버튼 위치 지정

        btn2 = QPushButton("Button 2", self) #버튼 만들기
        btn2.move(150, 50) #버튼 위치 지정

        btn1.clicked.connect(self.buttonClicked) #버튼 눌렸을때 실행되는거
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender() #sender() : buttonClicked를 호출한 객체(btn1, btn2)를 반환해주는 함수
        self.statusBar().showMessage(sender.text() + ' was pressed') #sender가 가지고 있는 text를 가져옴.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())