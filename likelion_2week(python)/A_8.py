latin_dic = {}
n = int(input())
for i in range(n):
    s = input().split(' - ')
    latin_dic[s[0]] = s[1].split(', ')
new_dict = {}
for k, v in latin_dic.items():
    for item in v:
        if item in new_dict:
            new_dict[item].append(k)
        else:
            new_dict[item] = [k]
print(len(new_dict))
for k, v in sorted(new_dict.items()):
    ans = ''
    print(k, '-', end=' ')
    for it in v:
        ans += it
        if len(v) > 1 and it != v[len(v) - 1]:
            ans += ', '
    print(ans)

# la_en = {}
# for _ in range(int(input())):
#   en_word, la_words = input().split(' - ')
#   for la_word in la_words.split(', '):
#     if la_word not in la_en:
#       la_en[la_word] = []
#     la_en[la_word].append(en_word)
# print(len(la_en))
# for la_word in sorted(la_en):
#   print(la_word, '-', ', '.join(sorted(la_en[la_word])))