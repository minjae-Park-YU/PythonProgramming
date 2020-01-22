from datetime import datetime

f = open("management.txt", 'a')
today = datetime.today().strftime("%Y%m%d")

date = []
index = []

while True:
    date.append(input("날짜 입력 : "))
    index.append(input("내용 입력 : "))
    a = input("나가기는 1번")
    if a == '1':
        break

f.write(date)
f.write(index)
f.close()