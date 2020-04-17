# def case1(n,a1,a2,a3):
#     for j in range(n):
#         if j == a1 or j == a2 or j == a3:
#             print("*", end=' ')
#         else:
#             print(".", end=' ')
#     print(sep='\n')
#
# def case2(n):
#     for j in range(0,n):
#         print('*', end=' ')
#     print(sep='\n')
#
# a = int(input())
# a1 = 0
# a2 = (a-1)/2
# a3 = (a-1)
# for i in range(a):
#     if i == a2:
#         case2(a)
#     elif i < a2:
#         case1(a,a1,a2,a3)
#         a1 += 1
#         a3 -= 1
#     else:
#         a3 += 1
#         a1 -= 1
#         case1(a,a1,a2,a3)




a = int(input())
b = [['.']*a for i in range(a)]
a1 = 0
a2 = (a-1)/2
a3 = (a-1)
flag = 1
for i in range(a):
    for j in range(a):
        if i == a2:
            b[i][j] = '*'
            flag = 0
        if j == a1 or j == a2 or j == a3:
            b[i][j] = '*'
    if flag == 1:
        a1 += 1
        a3 -= 1
    else:
        a1 -= 1
        a3 += 1
for line in b:
    print(*line)