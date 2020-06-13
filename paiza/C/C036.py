p1, p2 = [int(x) for x in input().split()]
p3, p4 = [int(x) for x in input().split()]

t = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]

second_p = []
if t[p1-1] > t[p2-1]:
    second_p.append(p2)
else:
    second_p.append(p1)

if t[p3-1] > t[p4-1]:
    second_p.append(p4)
else:
    second_p.append(p3)

second_p = sorted(second_p)

if f[0] > f[1]:
    second_p = reversed(second_p)

for i in second_p:
    print(i)