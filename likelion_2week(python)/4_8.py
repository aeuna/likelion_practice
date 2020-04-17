def fac(n):
    if n == 0:
        ans = 1
    else:
        ans = n * fac(n - 1)
    return ans


a = int(input())
sum = 0
for i in range(1, a + 1):
    sum += fac(i)
print(sum)
