s, A, B = [int(x) for x in input().split()]

while True:
    if s + 10 > A:
        P = "B"
        break
    s += 10
    if s + 1000 > B:
        P = "A"
        break
    s += 1000
print(P,s)