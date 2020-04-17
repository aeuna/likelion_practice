# n, m = [int(s) for s in input().split()]
# a = [['.' if (i + j) % 2 == 0 else '*']
#      for i in range(n)
#      for j in range(m)]
# for line in a:
#   print(*line)

def even(n):
    flag = 1
    for i in range(n):
        if flag == 1:
            print(".", end=' ')
            flag = 0
        else:
            print("*", end=' ')
            flag = 1
    print(sep='\n')


def odd(n):
    flag = 1
    for i in range(n):
        if flag == 1:
            print("*", end=' ')
            flag = 0
        else:
            print(".", end=' ')
            flag = 1
    print(sep='\n')


a, b = [int(s) for s in input().split()]

for i in range(a):
    if i % 2 == 0:
        even(b)
    else:
        odd(b)
