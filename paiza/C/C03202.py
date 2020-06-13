n = int(input())

v_list = [0,0,0,0]
for i in range(n):
    t, v = [int(x) for x in input().split()]
    num = v // 100
    if t == 0:
        v_list[0] += v
    elif t == 1:
        v_list[1] += v
    elif t == 2:
        v_list[2] += v
    elif t == 3:
        v_list[3] += v

total_point = 0
for i, value in enumerate(v_list):
    if i == 0:
        point = (value // 100) * 5
    elif i == 1:
        point = (value // 100) * 3
    elif i == 2:
        point = (value // 100) * 2
    elif i == 3:
        point = (value // 100) * 1
    total_point += point
print(total_point)