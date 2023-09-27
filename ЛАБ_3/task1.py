with open("F1.txt", 'w+') as F1:
    while True:
        a = input("Введите строку: ")
        if not a:
            break
        else:
            F1.write(a + "\n")

with open("F1.txt", 'r') as F1, open("F2.txt", 'w+') as F2:
    F1.seek(0)
    for line in F1:
        if line[-2] in ('A', 'a', 'А', 'а'):
            F2.write(line)
