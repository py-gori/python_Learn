N, M = (int(x) for x in input().split())

s_num = []
for i in range(1, N + 1):
    s_num.append(i)

goukaku = []
for i in range(len(s_num)):
    a, b = (int(x) for x in input().split())
    b *= 5
    score = a - b
    if score < 0:
        score = 0
        if score >= M:
            goukaku.append(s_num[i])
    elif score >= M:
        goukaku.append(s_num[i])

for i in goukaku:
    print(i)