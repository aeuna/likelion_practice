a = int(input("숫자를 입력해주세요"))
for i in range(1, a+1):
    sol = ""
    for k in range(i):
        sol += "*"
    print(sol.rjust(a))
