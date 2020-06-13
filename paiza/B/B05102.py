N = int(input())

circle = []
for i in range(N):
    line = [x for x in input().split()]
    circle.append(line)

sum_line = 0
for i in circle:
    if "0" not in i:
        tmp_line = [int(x) for x in i]
        sum_line = sum(tmp_line)

for j in range(len(circle)):
    if "0" in circle[j]:
        tmp = [i for i,x in enumerate(circle[j]) if x == "0"]
        if len(tmp) == 1:
            int_line = [int(x) for x in circle[j]]
            circle[j][tmp[0]] = str(sum_line - sum(int_line))
        elif len(tmp) == 2:
            for s in range(len(tmp)):
                sum_column = 0
                for k in range(len(circle)):
                    sum_column += int(circle[k][tmp[s]])
                    insert_num = str(sum_line - sum_column)
                circle[j][tmp[s]] = insert_num
for i in circle:
    print(*i)