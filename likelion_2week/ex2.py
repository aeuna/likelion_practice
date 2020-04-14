a, b, c = input("첫번째 [시,분,초]를 입력해주세요").split(",")
d, e, f = input("두번째 [시,분,초]를 입력해주세요").split(",")

sol1 = 3600*int(a) + 60*int(b) + int(c)
sol2 = 3600*int(d) + 60*int(e) + int(f)
print("두 시각의 시간 차이는", abs(sol1-sol2), "초 입니다!")
