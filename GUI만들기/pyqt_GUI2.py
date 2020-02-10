import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox #메시지 팝업창
from PyQt5.QtCore import QCoreApplication #버튼누르면 동작하게 하는 모듈 불러오기

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("push me!", self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(QCoreApplication.instance().quit) #클릭할때 꺼짐


        self.resize(500, 500)
        self.setWindowTitle("Sec Example")
        self.show()

    def closeEvent(self, QCloseEvent):
         ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) #메시지박스 창 두개
         if ans == QMessageBox.Yes: #Yes 누르면 꺼지고, No 누르면 안꺼짐
            QCloseEvent.accept()
         else:
            QCloseEvent.ignore()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())