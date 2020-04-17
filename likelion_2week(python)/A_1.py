dic = {}
a = input().split()
for i in range(0, len(a)):
    if a[i] in dic:
        print(dic[a[i]], end=' ')
        dic[a[i]] += 1
    else:
        dic[a[i]] = 1
        print(0, end=' ')
