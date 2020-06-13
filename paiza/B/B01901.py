n, k = [int(x) for x in input().split()]
org_a = []
for i in range(n):
    a = [int(x) for x in input().split()]
    org_a.append(a)

result = []
for i in range(0,n,k):
    for j in range(0,n,k):
        if i+1 < n:
            tmp = (sum(org_a[i][j:j+k]) + sum(org_a[i+1][j:j+k]))
            tmp //= k*2
            result.append(tmp)

def split_list(l, s):
    for i in range(0, len(l), s):
        yield l[i:i + s]
test = list(split_list(result, n // k))
for i in test:
    print(*i)