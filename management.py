from datetime import datetime

def fileread(date, sche):
    Date_f = open("Date.txt", 'r') #날짜 파일 읽기
    Sche_f = open("Sche.txt", 'r') #내용 파일 읽기
    date_t = Date_f.readlines()
    sche_t = Sche_f.readlines()
    for i in date_t:
        date.append(i[:-1])
    for ii in sche_t:
        sche.append(ii[:-1])
    Date_f.close()
    Sche_f.close()

def filewrite(date, sche):
    Date_f = open("Date.txt", 'w')
    Sche_f = open("Sche.txt", 'w')
    Date_f.write('\n'.join(date))
    Sche_f.write('\n'.join(sche))
    Date_f.close()
    Sche_f.close()

def filedelete(date, sche):
    Date_f = open("Date.txt", 'w')
    Sche_f = open("Sche.txt", 'w')
    Date_f.write('')
    Sche_f.write('')
    Date_f.close()
    Sche_f.close()

def matching(date, sche):
    today = datetime.today().strftime("%Y%m%d")  # 오늘 날짜
    leng = len(date)
    i = 0
    while i < leng:
        if not date:
            break
        elif today == date[i]:
            break
        i += 1
    if i > leng:
        print("오늘 일정이 없습니다.")
    elif not sche:
        print("오늘 일정이 없습니다.")
    else:
        print("오늘의 일정 : ", sche[i])

def sdelete(date, sche):
    date1 = date
    target = input("날짜를 입력해 주세요 : ")
    date.remove(target)
    i = 0
    leng = len(date)
    while i < leng:
        if not date:
            break
        elif date[i] != date1[i]:
           break
        i += 1
    i = i
    del sche[i]

def additional(date, sche):
    date.append(input("날짜 입력 : "))
    sche.append(input("내용 입력 : "))

def menu():
    print("1. 오늘 일정 확인   2. 일정 추가   3. 일정 삭제   4. 일정 초기화 후 저장  5. 일정 파일에 저장")


if __name__=="__main__":
    date = []
    sche = []
    fileread(date, sche)
    while True:
        menu()
        s = input()
        if s == '1':
            matching(date, sche)
        elif s == '2':
            additional(date, sche)
        elif s == '3':
            sdelete(date, sche)
        elif s == '4':
            filedelete(date, sche)
            break
        elif s == '5':
            filewrite(date, sche)
            break




