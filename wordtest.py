import random
we = open("english.txt", 'rt', encoding='cp949')
wk = open("korean.txt", 'rt', encoding='cp949')

wordlistE = we.read().splitlines()
wordlistK = wk.read().splitlines()
we.close()
wk.close()

def menu():
    print("1. 단어 입력   2. 단어 테스트   3. 단어장 초기화 후 종료   4. 단어장 저장 후 종료")

def inputword(wordlistE, wordlistK):
    wordlistE.append(input("영어 단어 입력 : "))
    wordlistK.append(input("뜻 입력 : "))

def wordtest(wordlistE, wordlistK):
    i = 0
    s = len(wordlistE)
    while i < s:
        p = random.randrange(0, s)
        print(wordlistE[p])
        answer = input("정답 입력 : ")
        if answer == wordlistK[p]:
            print("정답입니다.")
        else:
            print("오답입니다. 정답은 {} 입니다." .format(wordlistK[p]))
            i += 1

def resetword():
    we = open("english.txt", 'w')
    wk = open("korean.txt", 'w')
    we.write('')
    wk.write('')
    we.close()
    wk.close()

def saveword(wordlistE, wordlistK):
    we = open("english.txt", 'w')
    wk = open("korean.txt", 'w')
    we.write('\n'.join(wordlistE))
    wk.write('\n'.join(wordlistK))
    we.close()
    wk.close()

if __name__ == "__main__":
    while True:
        menu()
        select = input()
        if select == '1':
             inputword(wordlistE, wordlistK)
        elif select == '2':
             wordtest(wordlistE, wordlistK)
        elif select == '3':
            resetword()
            break
        else:
            saveword(wordlistE, wordlistK)
            break


