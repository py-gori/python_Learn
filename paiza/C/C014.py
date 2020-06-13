n, r = [int(x) for x in input().split()]

r_r = r * 2
result = []
for i in range(1, n+1):
    h, w, d = [int(x) for x in input().split()]
    if h >= r_r and w >= r_r and d >= r_r:
        result.append(i)

for i in result:
    print(i)