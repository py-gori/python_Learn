n, k = [int(x) for x in input().split()]
l = []
for i in range(n):
    a = [int(x) for x in input().split()]
    l.append(a)

sum_num = 0
f1 = 0
f2 = 0
ave_num = []
re_l = []
for _ in range(n*(n//k)):
    sum_num += sum(l[f1][f2:f2+k])
    f1 += 1
    if f1 % k == 0:
        ave_num.append(sum_num // (k*k))
        sum_num = 0
        if f1 == n:
            re_l.append(ave_num)
            ave_num = []
            f1 =0
            f2 += k
    else:
        pass
re_re_l = [list(x) for x in zip(*re_l)]

for i in re_re_l:
    print(*i)