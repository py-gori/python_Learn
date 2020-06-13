m, n, k = (int(x) for x in input().split())

M = {}
for i in range(m+1):
    M[i] = 0

M[0] = n
for i in range(k):
    speach_m = int(input())
    for j in range(0, m+1):
        if speach_m == j:
            count = 0
            for key, value in M.items():
                if value > 0:
                    count += 1
                    M[key] -= 1
            M[j] += count

values = []
for value in M.values():
    values.append(value)
values[0] = 0

max_value = max(values)

for i,x in enumerate(values):
    if x == max_value:
        print(i)