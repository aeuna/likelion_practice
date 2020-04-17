list1 = []
while 1:
    a = int(input())
    if a == 0:
        break
    list1.append(a)
sol = max(list1)
list1_set = set(list1)
list1 = list(list1_set)
list1.remove(sol)
print("두번째로 큰 값은", max(list1))