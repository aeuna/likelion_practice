# a = input().split()
# b = list(map(int, a))
# sol = [[int(j) for j in input().split()] for i in range(b[0])]
# list1 = list(map(max, sol))
# ans1 = list1.index(max(list1))
# ans2 = sol[ans1].index(max(list1))
# print(ans1, end=' ')
# print(ans2)

m, n = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
max_value, max_i, max_j = a[0][0], 0, 0
for i in range(m):
  for j in range(n):
    if a[i][j] > max_value:
      max_value, max_i, max_j = a[i][j], i, j
print(max_i, max_j)
