# def diagonal(ans1, ans2):
#     chk1 = 0
#     j = ans2
#     i = ans1
#     while j != 0:
#         i -= 1
#         j -= 1
#         if list[i][j] == 1:
#             chk1 = 1
#
#
#
#
#
#
#     for i in range(n):
#         for j in range(n):
#             if i < ans1 and j < ans2:
#                 if list[i][j] == 1:
#                     chk1 = 1
#                 i -= 1
#                 j -= 1
#             if i < ans1 and j > ans2:
#                 if list[i][j] == 1:
#                     chk1 = 1
#                 i -= 1
#                 j -= 1
#             if i > ans1 and j < ans2:
#                 if list[i][j] == 1:
#                     chk1 = 1
#                 i -= 1
#                 j -= 1
#             if i > ans1 and j > ans2:
#                 if list[i][j] == 1:
#                     chk1 = 1
#                 i -= 1
#                 j -= 1
#     return chk1


list = [[0 for j in range(8)] for i in range(8)]
chk = 0
for i in range(8):
    a = [int(s) for s in input().split()]
    list[8 - a[1]][a[0] - 1] = 1
    ans1 = 8 - a[1]
    ans2 = a[0] - 1
    for j in range(8):
        if list[j][a[0] - 1] == 1:
            if j != ans1:
                chk = 1
                print("1입니다")

        if list[8 - a[1]][j] == 1:
            if j != ans2:
                chk = 1
                print("2입니다")
        for k in range(8):
            if abs(j - k) == abs(ans1 - ans2) and j != k:
                if list[j][k] == 1:
                    print("---------------")
                    print(j, k)
                    print("---------------")
                    if j != ans1 and k != ans2:
                        chk = 1
                        print("3입니다")
    if chk == 1:
        break
if chk == 1:
    print("YES")
else:
    print("NO")
