N, M, K = [int(x) for x in input().split()]

posi = {str(x): 0 for x in range(1,M+1)}

for i in range(1, M+1):
    posi[str(i)] = int(input())

for k in range(K):
    for key, value in posi.items():
        for n in range(1,N+1):
            if not value + n > N:
                if value + n not in posi.values():
                    posi[key] = value + n
                    break
            elif value + n > N:
                if (value + n) - N not in posi.values():
                    posi[key] = (value + n) - N
                    break
for key, value in posi.items():
    print(value)