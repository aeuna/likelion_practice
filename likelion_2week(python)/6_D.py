save = []
while 1:
    n = int(input())
    if n == 0:
        break
    save.append(n)
print(save.count(max(save)))