# s = input().split(' - ')
# print(s)
# print(s[1].split(', '))
#
#
# n = int(input())
# a1 = 0
# a2 = (n-1)/2
# a3 = (n-1)
# flag = 1

# def case1(n):
#
# def case2(n):
#
# for i in range(n):
#     for j in range(n):
        if j == a1 or j == a2 or j == a3:
            print("*", end=' ')
        elif i == a2:
            print("*", end=' ')
            flag = 0
        else:
            print(".", end=' ')
    if flag == 1:
        a1 += 1
        a3 -= 1
    else:
        a1 -= 1
        a3 += 1
    print(sep='\n')

# for i in range(5):
#     print(i)
def solve(sol):
    chk = 0
    candidate = list(range(8))
    for i in range(len(sol)):
        if sol[i] in candidate:
            chk = 1
        distance = len(sol) - i
        if sol[i] + distance in candidate:
            chk = 1
        if sol[i] - distance in candidate:
            chk = 1
    if candidate != []:
        for i in candidate:
            sol.append(i)
            solve(sol)
    if chk == 1:
        print("YES")
    else:
        print("No")


for i in range(8):
    solve([i])
