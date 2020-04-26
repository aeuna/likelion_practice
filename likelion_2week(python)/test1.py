n = int(input("숫자를 입력하세요: "))
ans = 1
save = 1
while ans < n:
    save = save + 1
    ans = ans * save
print("곱의 결과 값이", n, "을 넘기 않는 가장 큰수는", save-1, "입니다.")
