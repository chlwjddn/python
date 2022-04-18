"""print("y = 3x**2 + 4*x + 1")
x = float(input("x의 값을 입력하시오: "))
y = 3*x**2 + 4*x + 1
print("함수값은 {}입니다".format(y))"""

time = int(input("초를 입력하세요: "))
h = time // 3600
m = (time % 3600) // 60
s = (time % 3600) % 60

print("지금은 %d시%d분%d초 입니다"%(h,m,s))