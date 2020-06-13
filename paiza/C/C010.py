a, b, R = [int(x) for x in input().split()]
koji = [a, b]

N = int(input())
result = []
for i in range(N):
    kokage = [int(x) for x in input().split()]
    anti = (kokage[0] - koji[0]) ** 2 + (kokage[1] - koji[1]) ** 2
    if anti >= R ** 2:
        result.append("silent")
    else:
        result.append("noisy")
for i in result:
    print(i)