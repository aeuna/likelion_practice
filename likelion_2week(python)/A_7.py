dic = {}
reverse = []
n = int(input())
for i in range(n):
    list1 = []
    list1 = input().split()
    for j in range(len(list1)):
        if list1[j] in dic:
            dic[list1[j]] += 1
        else:
            dic[list1[j]] = 1

sol = sorted(dic.items(), key=lambda x: x[1], reverse=True)

i = 0
while i < len(sol):
    sol_list = []
    cnt = 0
    for p in range(0, len(sol)):
        cnt += sol[p].count(sol[i][1])
    if cnt == 0:
        print(sol[i][0], [i][1])
        i += 1
    else:
        for j in range(cnt):
            sol_list.append(sol[i])
            i += 1
        sol_list.sort()
        for k in range(len(sol_list)):
            print(sol_list[k][0], sol_list[k][1])

# frequency = {}
# for _ in range(int(input())):
#   for word in input().split():
#     if word not in frequency:
#       frequency[word] = 0
#     frequency[word] += 1
# for i in sorted(set(frequency.values()), reverse=True):
#   for word in sorted([word for word in frequency if frequency[word] == i]):
#     print(word, i)



# sol_list = []
# for i in range(1, n):
#     cnt = sol.count(sol[i][])
#
#
#     if sol[i-1][1] == sol[i][1]:
#         sol_list.append(sol[i])
#     else:
#         sol_list.sort()
#         if sol_list:
#             print(sol_list)
#             sol_list = []
#         print(sol[i][0], sol[i][1])

# for k, l in sol:

# for a, b in dic.items():
#     reverse.append([b, a])
# print(sorted(reverse))
