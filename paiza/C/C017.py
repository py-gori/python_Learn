a, b = [int(x) for x in input().split()]
n = int(input())

for i in range(n):
    A, B = [int(x) for x in input().split()]
    if a > A:
        print("High")
    elif a < A:
        print("Low")
    elif a == A:
        if b < B:
            print("High")
        elif b > B:
            print("Low")