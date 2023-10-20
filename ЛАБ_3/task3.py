import re

with open("study.txt", 'r', encoding="utf-8") as f:
    name = list()
    av = list()

    dic = dict()
    for line in f:
        #arr = re.split("[^0-9]+", line)
        #print(re.match("\\w", line))
        #print(arr)
        num = ""
        num1 = ""
        num2 = ""
        aver = 0
        a = line.strip().split()
        word = ""
        for ch in a[0]:
            if ch != ':':
                word = word + ch
        if len(a) == 2:

            for ch in a[1]:
                if ch.isdigit():
                    num = num + ch
                aver = int(num)

        if len(a) == 3:
            for ch in a[1]:
                if ch.isdigit():
                    num = num + ch

            for ch in a[2]:
                if ch.isdigit():
                    num1 = num1 + ch
            aver = int(num) + int(num1)

        if len(a) == 4:

            for ch in a[1]:
                if ch.isdigit():
                    num = num + ch

            for ch in a[2]:
                if ch.isdigit():
                    num1 = num1 + ch
            for ch in a[3]:
                if ch.isdigit():
                    num2 = num2 + ch
            aver = int(num) + int(num1) + int(num2)
        name.append(word)
        av.append(aver)

i = 0
for i in range(len(name)):
    dic[name[i]] = av[i]
print(dic)
