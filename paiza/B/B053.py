# 表の自動生成
line, column = (int(x) for x in input().split())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

list_ab = [list(a),list(b)]
for i in range(2,line):
    L = []
    for j in range(2):
        l = list_ab[i-1][j] + (list_ab[i-1][j] - list_ab[i-2][j])
        L.append(l)
    list_ab.append(L)
list_answer = []
for i in list_ab:
    for j in range(2,column):
        i.append(i[j-1] + (i[j-1] - i[j-2]))
    list_answer.append(i)

for i in list_answer:
    i = [str(x) for x in i]
    result = " ".join(i)
    print(result)