n, x = (int(x) for x in input().split())

t = []
for i in range(n):
    s = input().split()
    X = x - int(s[0])
    if X < 0:
        t.append(int(s[1]))
    else:
        X2 = X // int(s[2])
        X2 += 1
        X3 = X2 * int(s[3])
        X3 += int(s[1])
        t.append(X3)
result_L = []
result_L.append(min(t))
result_L.append(max(t))
result = map(str, result_L)
result_t = " ".join(result)
print(result_t)