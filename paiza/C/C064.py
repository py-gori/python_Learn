m, n = [int(x) for x in input().split()]

Cal = []
for i in range(m):
    c = int(input())
    c = c / 100
    Cal.append(c)

import math
n_c = []
for i in range(n):
    eat = [int(x) for x in input().split()]
    total_c = 0
    for j in range(m):
        calolie = Cal[j] * eat[j]
        calolie = math.floor(calolie)
        total_c += calolie
    n_c.append(total_c)

for i in n_c:
    print(i)