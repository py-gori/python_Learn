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
import numpy as np
result_np = np.array(result).reshape(n // k,n // k)
for i in result_np:
    print(*i)
