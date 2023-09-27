import json
with open("firm.txt",'r', encoding="utf-8") as f:
    name = []
    prib = []
    dic1 = dict()
    dic2 = dict()
    for line in f:
        a = line.strip().split()
        pribyl = int(a[2])-int(a[3])
        name.append(a[0])
        prib.append(pribyl)
        i =0
    for i in range(len(name)):
        dic1[name[i]] = prib[i]
    count = 0
    av_p = 0
    for el in prib:
        av_p = av_p+el
        count = count + 1
    av_p = int(av_p/count)
    dic2["average_profit"] = av_p
    mainl = list()
    mainl.append(dic1)
    mainl.append(dic2)
    print(mainl)
with open("firm2.json", 'w', encoding="utf-8") as f2:

    json.dump(mainl,f2)
