n = int(input())
h, w = [int(x) for x in input().split()]

room = []
for i in range(h):
    line = input()
    room.append(line)

clear = 0
for i in room:
    for j in range(w):
        if room[0][j] == "#":
            clear += 1
            n -= 1
            if n == 0:
                break
        else:
            n -= 1
            if n == 0:
                break
    for s in range(h):
        if room[s][w-1] == "#":
            clear += 1
            n -= 1
            if n == 0:
                break
        else:
            n -= 1
            if n == 0:
                break
    for k in range(w-1,0,-1):
        if room[h-1][k] == "#":
            clear += 1
            n -= 1
            if n == 0:
                break
        else:
            n -= 1
            if n == 0:
                break
    for l in range(h-1,1,-1):
        if room[l][0] == "#":
            clear += 1
            n -= 1
            if n == 0:
                break
        else:
            n -= 1
            if n == 0:
                break
print(clear)
print(n)