N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
Q = int(input())

for i in range(Q):
    Q_s, Q_e = [int(x) for x in input().split()]
    sum = 0
    for j in range(Q_s -1,Q_e):
        sum += A[j]
    w = Q_e - Q_s + 1
    sabun = M - (sum // w)
    if sabun > 0:
        for k in range(Q_s -1,Q_e):
            A[k] += sabun
print(*A)