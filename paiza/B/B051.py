N = int(input())

num_m = []
for i in range(N):
    num = [int(x) for x in input().split()]
    num_m.append(num)

# 辺の最大値を求める
for i in range(N):
    if 0 not in num_m[i]:
        sum_m = sum(num_m[i])
        break

num_str = [str(x) for x in num_m]
for i in range(N):
    for j in range(N):
        if num_m[i][j] == 0:
            if num_str[i].count("0") == 1:
                tmp = sum_m - sum(num_m[i])
                num_m[i][j] = tmp
            elif num_str[i].count("0") > 1:
                num_k = 0
                for k in range(N):
                    num_k += num_m[k][j]
                tmp = sum_m - num_k
                num_m[i][j] = tmp

for i in num_m:
    print(*i)