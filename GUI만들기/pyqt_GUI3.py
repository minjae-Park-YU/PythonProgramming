import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu #위젯 대신 메인윈도우로 사용
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar() #상태표시줄
        self.statusBar().showMessage("Hello") #하단에 글씨 생김

        #메뉴바 생성 - 1
        menu = self.menuBar() #상단 메뉴바 만들기
        menu_File = menu.addMenu("File") #메뉴바 큰 그룹 생성
        menu_Edit = menu.addMenu("Edit")

        #메뉴 세부 동작 생성 - 3
        File_exit = QAction('Exit', self) #메뉴 객체 생성
        File_exit.setShortcut('Ctrl+Q')
        File_exit.setStatusTip("누르면 영원히 빠이빠이")
        new_txt = QAction("텍스트 파일", self)
        new_py = QAction("파이썬 파일", self)

        File_exit.triggered.connect(QCoreApplication.instance().quit)

        #서브 그룹 만들기, 객체 만들기 - 3
        File_new = QMenu('New', self)
        File_new.addAction(new_txt)
        File_new.addAction(new_py)

        #주 메뉴 추가(그룹) - 2
        menu_File.addMenu(File_new)   #Action과 New의 차이 : Action -> 바로 동작, New -> 세부항목으로 들어감
        menu_File.addAction(File_exit)  #메뉴 등록
        self.resize(450, 400)
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())