M,N = [int(x) for x in input().split()]

result = 0
for i in range(1,M):
    for j in range(1,N):
        x = (i**2) + (j**2)
        x = x ** (1/2)
        if x.is_integer() == True:
            result += 1
print(result)