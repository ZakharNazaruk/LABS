with open("info.txt", 'r', encoding="utf-8") as my_f:
    name = list()
    mark = list()
    for line in my_f:
        a = line.strip().split()
        name.append(a[0])
        mark.append(a[1])
print("Ученики со средним баллом от 4 до 6:")
i = 0
for i in range(len(mark)):

    if 4 <= float(mark[i]) < 6:
        print(name[i])

print("\nУченики со средним баллом от 6 до 8:")
i = 0
for i in range(len(mark)):

    if float(mark[i]) >= 6 and float(mark[i]) < 8:
        print(name[i])
print("\nУченики со средним баллом от 8 и выше:")
i = 0
for i in range(len(mark)):

    if float(mark[i]) >= 8:
        print(name[i])
a = max(mark)
ind = mark.index(a)
print(f"\nСтудент с максимальным средним баллом: {name[ind]} \nего средний балл состовляет: {a}")
