n = int(input())
tefuda_l = []
for i in range(n):
    tefuda = input()
    tmp_a = []
    for j in tefuda:
        tmp_a.append(int(j))
    tefuda_l.append(tmp_a)

for i in tefuda_l:
    if i.count(i[0]) == 4:
        print("Four Card")
    elif i.count(i[0]) == 3 or i.count(i[1]) == 3 or i.count(i[2]) == 3 or i.count(i[3]) == 3:
        print("Three Card")
    elif i.count(i[0]) == 2 and i.count(i[2]) == 2:
        print("Two Pair")
    elif i.count(i[0]) == 2 or i.count(i[1]) == 2 or i.count(i[2]) == 2 or i.count(i[3]) == 2:
        print("One Pair")
    else:
        print("No Pair")