limit = 539 # 08:59
a, b, c = (int(x) for x in input().split())

train_n = int(input())

train_list = []
for i in range(train_n):
    h, m = (int(x) for x in input().split())
    train_time = (h * 60) + m
    train_list.append(train_time)

TMP = []
for i in range(len(train_list)):
    tmp = limit - (b + c)
    if tmp - train_list[i] > 0:
        TMP.append(train_list[i])
S = max(TMP) - a
S_h = str(S // 60)
S_m = str(S % 60)
print(S_h.rjust(2, "0") + ":" + S_m.rjust(2, "0"))