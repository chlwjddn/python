#1
'''age = int(input("나이를 입력해주세요: "))

if age >= 70:
    print("경로 우대 승차권 발급")
else:
    print("일반승차권입니다")
print("이용해주셔서 감사합니다")'''

#2

'''gpa = float(input("평균학점을 입력하세요: "))
toeic = int(input("토익점수을 입력하세요: "))

if gpa >= 4.0 and toeic >= 800 :
    print("지원가능합니다")
else:
    print("지원할 수 없습니다")'''

#3

'''dic = {"영국":70,"프랑스":80,"이탈리아":80,"스위스":90}

print(dic.keys())

nation = str(input("여행할 국가를 입려하세요:"))
date = int(input("출국 전 남은 날짜를 입력하세요: "))

if date >= 30:
    print("납부하실 금액은{}입니다".format(dic[nation]*0.8))
elif date >= 15:
    print("납부하실 금액은{}입니다".format(dic[nation]*0.9))  
else:
    print("납부하실 금액은{}입니다".format(dic[nation]))'''

#4

origin_id = str(input("아이디를 입력하세요: "))
origin_pw = str(input("비밀번호를 입력하세요: "))

tested_id = str(input("아이디를 입력하세요"))
tested_pw = str(input("비밀번호를 입력하세요"))


if origin_id == tested_id and origin_pw == tested_pw :
    print("로그인 성공")
else:
    print("로그인 실패")





