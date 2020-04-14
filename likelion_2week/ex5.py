a = input("숫자를 입력해주세요").split()
b = list(map(int, a))

sol1 = max(b)
sol2 = min(b)

print("최댓값은:", sol1, "위치는:", b.index(sol1))
print("최솟값은:", sol2, "위치는:", b.index(sol2))
