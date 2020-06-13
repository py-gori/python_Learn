L = input().split()

in_x = L.index("x")

if L[1] == "+":
    if in_x == 0:
        x = int(L[4]) - int(L[2])
    elif in_x == 2:
        x = int(L[4]) - int(L[0])
    elif in_x == 4:
        x = int(L[0]) + int(L[2])

if L[1] == "-":
    if in_x == 0:
        x = int(L[4]) + int(L[2])
    elif in_x == 2:
        x = int(L[4]) - int(L[0])
    elif in_x == 4:
        x = int(L[0]) - int(L[2])
print(x)