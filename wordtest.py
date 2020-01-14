import random

wordlistE = [] #영어 단어 저장 리스트
wordlistK = [] #영어 단어 뜻 저장 리스트

def menu():
    print("1. 단어 입력   2. 단어 테스트   3. 종료")

def inputword():
    wordlistE.append(input("영어 단어 입력 : "))
    wordlistK.append(input("뜻 입력 : "))

def wordtest(wordliseE, wordliseK):
    i = 0
    s = len(wordlistE)
    while i < s:
        p = random.randrange(0, s)
        print(wordlistE[p])
        answer = input("정답 입력 : ")
        if answer == wordliseK[p]:
            print("정답입니다.")
        else:
            print("오답입니다. 정답은 {} 입니다." .format(wordlistK[p]) )
        i += 1

while True:
    menu()
    select = input()
    if select == '1':
        inputword()
    elif select == '2':
        wordtest(wordlistE, wordlistK)
    else:
        break
