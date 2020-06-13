n, k = [int(x) for x in input().split()]
org_a = []
for i in range(n):
    a = [int(x) for x in input().split()]
    org_a.append(a)

tmp = 0
result = []
for i in range(0,n,k):
    for j in range(n):
        tmp += sum(org_a[j][i:i + k])
        if (j+1) % k == 0:
            tmp //= k
            tmp //= k
            result.append(tmp)
            tmp = 0

def split_list(l, s):
    for i in range(0, len(l), s):
        yield l[i:i + s]
test = list(split_list(result, n // k))
for i in test:
    print(*i)