Q = int(input())

for i in range(Q):
    int_N = int(input())

    D_num = []
    i = 0
    while True:
        i += 1
        if int_N <= i:
            break
        if int_N % i == 0:
            D_num.append(i)

    if sum(D_num) == int_N:
        print("perfect")
    elif sum(D_num) + 1 == int_N:
        print("nearly")
    else:
        print("neither")