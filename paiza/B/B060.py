n, h, w = [int(x) for x in input().split()]
sy, sx = [int(x) - 1 for x in input().split()]
direction = input()
flag = []
for i in range(h):
    flag_line = []
    for j in range(w):
        flag_line.append(0)
    flag.append(flag_line)

num = 6
flag[sy][sx] = 6
for j in direction:
    if j == "U":
        sy -= 1
    elif j == "D":
        sy += 1
    elif j == "R":
        sx += 1
    elif j == "L":
        sx -= 1
    flag[sy][sx] = num
print(flag)