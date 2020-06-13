w = int(input())
head = input().split()
h = int(input())
table = []
table.append(head)
for i in range(h):
    data = [str(x) for x in input().split()]
    table.append(data)

len_list = []
for i in range(len(table[0])):
    max_len = 0
    for j in range(len(table)):
        length = len(table[j][i])
        if length > max_len:
          max_len = length
    len_list.append(max_len)

kugiri_l = []
for i in len_list:
    haihun = "-"
    haihun = (haihun * i) + "--"
    kugiri_l.append(haihun)

for i in range(len(table[0])):
    for j in range(len(table)):
        table[j][i] = " " + table[j][i].ljust(len_list[i] + 1," ")
table.insert(1,kugiri_l)

for i in table:
    k = "|".join(i)
    print("|" + k + "|")