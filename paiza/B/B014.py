X, Y, Z = [int(x) for x in input().split()]

printer = []
for z in range(Z):
    x = []
    for i in range(X):
        line = input()
        x.append(line)
    printer.append(x)
    kugiri = input()

answer = []
for i in range(Z-1,-1,-1):
    tmp_ = ["." for i in range(Y)]
    for j in range(X):
        line = printer[i][j]
        for y in range(Y):
            if line[y] == "#":
               tmp_[y] = "#"
    tmp = "".join(tmp_)
    answer.append(tmp)
for i in answer:
    print(i)

'''
for i in range(Z-1,-1,-1):
    old_count = 0
    for j in range(X):
        count_ = printer[i][j].count("#")
        if count_ >= old_count:
            old_count = count_
            max_in = j
    answer.append(printer[i][max_in])

for i in answer:
    print(i)
'''