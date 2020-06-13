n = int(input())

point = 0
for i in range(n):
    d, p = input().split()
    if "3" in d:
        point += int(p) * (3 / 100)
        point = int(point)
    elif "5" in d:
        point += int(p) * (5 / 100)
        point = int(point)
    else:
        point += int(p) * (1 / 100)
        point = int(point)
print(point)