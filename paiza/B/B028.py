# n = 社員数, g = グループ数, m = メッセージ数
n, g, m = [int(x) for x in input().split()]

if g != 0:
    group_list = []
    for i in range(g):
        g_mem, mem = input().split(" ",1)
        mem = [int(x) for x in mem.split()]
        group_list.append(mem)
message_list = []
for i in range(m):
    message = [int(x) if str.isnumeric(x) else x for x in input().split()]
    message[0] = message[0] - 1
    message[2] = message[2] - 1
    message_list.append(message)

# メッセージ出力用空リスト作成
out_message = []
for i in range(n):
    i = []
    out_message.append(i)

# メンバ毎にメッセージ格納
for i in message_list:
    if i[1] == 0:
        for j in range(n):
            if i[0] == j or i[2] == j:
                out_message[j].append(i[3])
    if i[1] == 1:
        for j in range(g):
            if i[2] == j:
                for k in group_list[j]:
                    out_message[k-1].append(i[3])

count = 0
for i in out_message:
    for j in i:
        print(j)
    count += 1
    if count != len(out_message):
            print("--")