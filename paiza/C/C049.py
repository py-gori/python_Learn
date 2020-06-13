line = int(input())

for i in range(line):
    floor = int(input())
    if i == 0:
        mv = floor - 1
    else:
        if floor > old_floor:
            mv = floor - old_floor + mv
        else:
            mv = old_floor - floor + mv
    old_floor = floor
print(mv)