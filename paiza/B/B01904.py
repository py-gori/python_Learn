n, k = [int(x) for x in input().split()]
l = []
for i in range(n):
    a = [int(x) for x in input().split()]
    l.append(a)

sum_num = 0
f1 = 0
f2 = 0
re_l = []
for _ in range(n*n):
    sum_num += sum(l[f1][f2:f2+k])
    f1 += 1
    if f % k == 0:
        ave_num = sum_num // (k*k)
        re_l.append(ave_num)
        sum_num = 0

        f1 =0
        f2 += k
    else:
        pass
print(re_l)