class Person:
    def __init__(self, name): #생성자, 여기에 name처럼 변수 추가하면 객체 지정시 초기화 가능
        self.name = name #이렇게 self로 스스로 객체생성하고 할당가능

    def say_hello(self, to_name): #함수 사용, 마찬가지로 괄호안에 변수넣어주면 사용시 초기화하면서 사용가능
        print("안녕! " + to_name +  " 나는 " + self.name + "(이)야")

wonie = Person("워니") #여기서 wonie라는 객체를 지정하고, 그와 동시에 "워니"라는 것으로 생성자 만듬.
micheal = Person("마이클")
jenny = Person("제니")

wonie.say_hello("철수")  #아까 만든 객체를 사용하여 클래스 내부 함수를 사용한 모습
micheal.say_hello("영희")
jenny.say_hello("미지")