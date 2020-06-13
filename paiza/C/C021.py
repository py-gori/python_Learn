xc, yc, r1, r2 = [int(x) for x in input().split()]
n = int(input())

result = []
for i in range(n):
    place = [int(x) for x in input().split()]
    x = (place[0] - xc) * (place[0] - xc)
    y = (place[1] - yc) * (place[1] - yc)
    if r1*r1 <= x + y <= r2*r2:
        result.append("yes")
    else:
        result.append("no")
for i in result:
    print(i)