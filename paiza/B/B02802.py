n, g, m = [int(x) for x in input().split()]

group = []
if g != 0:
    for i in range(g):
        gmem, mem  = input().split(" ",1)
        mem = [int(x) for x in mem.split()]
        group.append(mem)

message_list = []
for i in range(m):
    message = input().split()
    message[0] = int(message[0]) - 1
    message[1] = int(message[1])
    message[2] = int(message[2]) - 1
    message_list.append(message)

out_message = []
for i in range(n):
    i = []
    out_message.append(i)

for j in message_list:
    if j[1] == 0:
        for k in range(n):
            if j[0] == k or j[2] == k:
                out_message[k].append(j[3])
    elif j[1] == 1:
        for l in range(len(group)):
            if j[2] == l:
                for s in group[l]:
                    out_message[s-1].append(j[3])
count = 0
for i in out_message:
    for j in i:
        print(j)
    count += 1
    if count != len(out_message):
        print("--")