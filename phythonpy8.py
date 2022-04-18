#딕션너리 실습 문제

CU = {"사탕":200,"껌":500,"아이스크림":1000}

print(CU.keys())

menu = input("메뉴를 고르시오: ")

print(CU[menu])

#세트 도전 문제

clubA = {"kim","park","hwang"}
clubB = {"park","lee","choi"}

clubC = clubA | clubB
print(clubC)

print(clubA&clubB)

print(clubA-clubB)

print(clubB-clubA)

clubA.add("yang")
clubB.remove("lee")

print(clubA)
print(clubB)

