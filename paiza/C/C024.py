SET1 = 0
SET2 = 0

n = int(input())

for i in range(n):
    order = input().split()
    if order[0] == "SET":
        if order[1] == "1":
            SET1 = int(order[2])
        elif order[1] == "2":
            SET2 = int(order[2])
    elif order[0] == "ADD":
        SET2 = SET1 + int(order[1])
    elif order[0] == "SUB":
        SET2 = SET1 - int(order[1])

print(SET1, SET2)