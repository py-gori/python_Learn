n = int(input())

data_l = []
for i in range(n):
    data = [int(x) for x in input().split()]
    data_l.append(data)

start = data_l[0][0]
finish = data_l[-1][1]

high = 0
low = 0
for i in data_l:
    high_tmp = i[2]
    low_tmp = i[3]
    if high_tmp > high:
        high = high_tmp
    if low_tmp < low or low == 0:
        low = low_tmp
print(start,finish,high,low)