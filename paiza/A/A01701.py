h, w, n = [int(x) for x in input().split()]

result = []
for i in range(h):
    result_line = []
    for j in range(w):
        result_line.append(".")
    result.append(result_line)

for i in range(n):
    H, W, X = [int(x) for x in input().split()]
    for h_i in range(h):
        for w_i in range(W):
            if "#" not in result[h_i][X+w_i]:
                f = "True"
            else:
                f = "False"
                break
    if f == "True":
        for s in range(H):
            for t in range(W):
                result[h_i-s][X+t] = "#"
        break
for i in result:
    for j in i:
        print(j,end="")
    print("")
