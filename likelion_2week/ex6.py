sc = int(input("점수를 입력해주세요: "))
if 90 <= sc <= 100:
    point = "A"
elif 80 <= sc <= 89:
    point = "B"
elif 70 <= sc <= 79:
    point = "C"
elif 60 <= sc <= 69:
    point = "D"
else:
    point = "F"

print(sc, "점은", point, "입니다")
