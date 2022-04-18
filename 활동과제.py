#1

'''degree = int(input("현재온도를 입력하세요:" ))

if degree >= 25:
    print("반바지 추천")
else:
    print("긴바지 추천")'''

#2

'''origin_id = str(input("아이디를 입력하세요: "))
origin_pw = str(input("비밀번호를 입력하세요: "))

tested_id = str(input("아이디를 입력하세요"))
tested_pw = str(input("비밀번호를 입력하세요"))


if origin_id == tested_id and origin_pw == tested_pw :
    print("로그인 성공")
else:
    print("로그인 실패")'''

#3

'''math = int(input("수학점수를 입력하시오: "))
english = int(input("영어 점수를 입력하시오: "))

if math >= 80 and english >= 80:
    print("합격")
else:
    print("불합격")'''

#4

"""price = int(input("총 구입금액을 입력하세요: "))

print(f"총 구입금액은 {price}원입니다")

if price >= 100000:
    print(f"할인금액은 {int(price*0.05)}원입니다")
    print(f"지불금액은 {int(price*0.95)}원입니다")
else:
    print(f"할인금액은 0원입니다")
    print(f"지불금액은 {price}원입니다")"""

#5

'''attendance = int(input('출석 점수를 입력하세요: '))
quiz = int(input('퀴즈 점수를 입력하세요: '))
assignment = int(input('과제 점수를 입력하세요: '))
final_exam = int(input('기말고사 점수를 입력하세요: '))

print('출석점수: %s'% attendance)
print('퀴즈점수: %s'% quiz)
print('과제점수: %s'% assignment)
print('기말점수: %s'% final_exam)


grade = (attendance+ quiz + assignment)*0.2 + final_exam*0.4

if grade >= 90:
    print("grade = A학점")
elif grade >= 80:
    print("grade = B학점")
elif grade >= 70:
    print("grade = C학점")
else:
    print("grade = F학점")'''

#6

'''price = int(input("지불금액을 입력해주세요: "))
print("구매금액: %d"%price)


if price >= 200000:
    discount = 0.8*price
    discount_percentage = 20
elif price >= 50000:
    discount = 0.9*price
    discount_percentage = 10
elif price> 10000:
    discount = 0.95*price
    discount_percentage = 5
else:
    discount = price
    discount_percentage = 0

print("할인율: {}%".format(discount_percentage))
print(f"할인 금액: {price - discount}")
print("지불금액: {}".format(discount))'''

#7

'''time = int(input("근무시간: "))
pay = int(input("시간당 임금: "))
print(f"근무시간: {time}")
print(f"시간당 임금: {pay}")

if time <= 40:
    total_pay = time * pay
else:
    total_pay = (time -40) * (pay*1.5) + pay*40

print(f"total pay: {int(total_pay)}")'''

#8



