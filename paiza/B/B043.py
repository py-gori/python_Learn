H, W = [int(x) for x in input().split()]
h0, w0 = [int(x) for x in input().split()]
h0 -= 1
w0 -= 1

# . = 庶民（右へ）* = 富豪（左へ）
h_l = []
for i in range(H):
    h_type = input()
    h_type = list(h_type)
    h_l.append(h_type)

while True:
    # 北=1 東=2　南=3　西=4
    direction = 1
    for i in range(2000):
        try:
            h_l[h0][w0] == "."
        except IndexError:
            break
        else:
            if direction == 1:
                if h_l[h0][w0] == ".":
                    h_l[h0][w0] = "*"
                    w0 += 1
                    direction += 1
                elif h_l[h0][w0] == "*":
                    h_l[h0][w0] = "."
                    w0 -= 1
                    direction += 3
            elif direction == 2:
                if h_l[h0][w0] == ".":
                    h_l[h0][w0] = "*"
                    h0 += 1
                    direction += 1
                elif h_l[h0][w0] == "*":
                    h_l[h0][w0] = "."
                    h0 -= 1
                    direction -= 1
            elif direction == 3:
                if h_l[h0][w0] == ".":
                    h_l[h0][w0] = "*"
                    w0 -= 1
                    direction += 1
                elif h_l[h0][w0] == "*":
                    h_l[h0][w0] = "."
                    w0 += 1
                    direction -= 1
            elif direction == 4:
                if h_l[h0][w0] == ".":
                    h_l[h0][w0] = "*"
                    h0 -= 1
                    direction -= 3
                elif h_l[h0][w0] == "*":
                    h_l[h0][w0] = "."
                    h0 += 1
                    direction -= 1
        if i == 1999:
            break
    break
for i in h_l:
    result = "".join(i)
    print(result)