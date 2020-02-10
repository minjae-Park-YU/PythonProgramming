import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton #기본적으로 가져와야할것 : 앞에꺼 두개

class Exam(QWidget): #내가 만들고 싶은 클래스(상속 받아서 쓰는거임)
    def __init__(self): #생성자
        super().__init__() #상위 객체 생성
        self.initUI()

    def initUI(self):
        btn = QPushButton('click', self) #버튼 추가
        btn.resize(btn.sizeHint()) #위에 click 글씨를 기준으로 자동으로 크기설정
        btn.setToolTip('This Tooltip.<b>Hello.<b/>') #뒤에꺼는 볼드체
        btn.move(20, 30) #창 크기 이동, 순서는 왼쪽, 위에서의 거리

        self.setGeometry(300, 300, 400, 500) #전체 창 크기 조절(창위치, 창위치, 가로, 세로)
        self.setWindowTitle('first time')
        self.show() #눈에 보이게 창 띄우는거

app = QApplication(sys.argv)  #어플 객체 생성이 제일 처음 단계
w = Exam() #클래스 객체 지정
sys.exit(app.exec_()) #프로그램 종료 후 리턴값, app.exec_() : 이벤트정보를 전달하기 위한 루프(메인루프)

