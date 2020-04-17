dic = {}
for i in range(int(input())):
    l, k = input().split()
    if l in dic.keys():
        dic[l] += int(k)
    else:
        dic[l] = int(k)
dic1= sorted(dic.items())
for a, b in dic1:
    print(a, b)
