N, M = [int(x) for x in input().split()]

pay_list = []
for i in range(M):
    pay = int(input())
    pay_list.append(pay)

point = 0
for c in pay_list:
    if point >= c:
        point -= c
    else:
        N -= c
        point = int(point + (c * 0.1))
    print(N, point)