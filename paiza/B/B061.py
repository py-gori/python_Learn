S = int(input())
N = int(input())

V = []
for i in range(N):
    v = int(input())
    V.append(v)

Sums = []
for i in range(N):
    for j in range(i+1, N):
        sum_2 = V[i] + V[j]
        if sum_2 >= S:
            if sum_2 - V[i] < S or sum_2 - V[j] < S:
                Sums.append(sum_2)
    for k in range(i+2, N):
        sum_3 = V[i] + V[j] + V[k]
        if sum_3 >= S:
            if sum_3 - V[i] < S or sum_3 - V[j] < S or sum_3 - V[k] < S:
                Sums.append(sum_3)
    if N > 3:
        for l in range(i+3, N):
            sum_4 = V[i] + V[j] + V[k] + V[l]
            if sum_4 >= S:
                if sum_4 - V[i] < S or sum_4 - V[j] < S or sum_4 - V[k] < S or sum_4 - V[l] < S:
                    Sums.append(sum_4)

print(Sums)
'''
Sums = []
for i in range(N):
    sums = 0
    for j in range(i+1, N):
        sum_1 = V[i] + V[j]
        if sum_1 >= S:
            if sum_1 - V[i] < S or sum_1 - V[j] < S:
                Sums.append(sum_1)
        sums += V[j]
        if sums >= S:
            if S > sums - V[i] or S > sums - V[j]:
                Sums.append(sums)
print(Sums)
'''
'''Sums = []
for i, num_1 in enumerate(V):
    Sums.append(num_1)
    Sums.append(sum(V))
    for j, num_2 in enumerate(V):
        if i != j:
            num_1 += num_2
'''
