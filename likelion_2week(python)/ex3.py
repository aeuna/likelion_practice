number = int(input("두자리 숫자를 입력해 주세요:"))
a = number//10
b = number % 10
print(a, end=' ')
print(b)
sol = str(b) + str(a)
print(sol)
