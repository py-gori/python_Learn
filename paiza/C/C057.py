t, x, y = [int(x) for x in input().split()]
x_y = list((x, y))
max_x = x
point = []
for _ in range(t):
    tmp_xy = [int(x) for x in input().split()]
    point.append(tmp_xy)

for i in range(len(point)):
    x_y[0] += point[i][0]
    x_y[1] += point[i][1]
    if x_y[0] > max_x:
        max_x = x_y[0]
    if x_y[1] <= 0:
        break
print(max_x)