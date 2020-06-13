n = int(input())

dict_list = {0:0, 1:0, 2:0, 3:0}
for i in range(n):
    t, v = [int(x) for x in input().split()]
    if t == 0:
        dict_list[0] += v
    elif t == 1:
        dict_list[1] += v
    elif t == 2:
        dict_list[2] += v
    elif t == 3:
        dict_list[3] += v

total_point = 0
for key, value in dict_list.items():
    num = value // 100
    if key == 0:
        point = num * 5
    elif key == 1:
        point = num * 3
    elif key == 2:
        point = num * 2
    elif key == 3:
        point = num * 1
    total_point += point

print(total_point)