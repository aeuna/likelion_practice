a = [int(s) for s in input().split()]
n = 0
while n < len(a):
    if a[n] % 2 == 0:
        print(a[n], end=' ')
    n += 1
