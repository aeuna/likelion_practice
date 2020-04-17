n = int(input())
dic = {}
for i in range(n):
    l, m = input().split()
    dic[l] = m
print(dic)
s = input()
for j, k in dic.items():
    if k == s:
        print(j)
    if j == s:
        print(k)

# synonyms = {}
# for i in range(int(input())):
#   w1, w2 = input().split()
#   synonyms[w1] = w2
#   synonyms[w2] = w1
# print(synonyms[input()])