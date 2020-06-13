m, n, x = [int(x) for x in input().split()]
w_l = []
for i in range(m):
    w = int(input())
    w_l.append(w)

taikyu = x
count = 0
for i in range(m):
    if taikyu - w_l[i] > 0:
        taikyu -= w_l[i]
        count += 1
    else:
        if n > 1:
            taikyu = x
            n -= 1
            if taikyu - w_l[i] > 0:
                taikyu -= w_l[i]
                count += 1
            else:
                break
        else:
            break
print(count)