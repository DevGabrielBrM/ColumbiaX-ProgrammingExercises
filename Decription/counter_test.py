from collections import Counter

list = [x for x in range(100)]
print(list)

for x in range(15):
    list.append("a")
    x+=1
list_c = Counter(list)

print(list_c)
print(list_c['a'])