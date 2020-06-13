import math

x, p = [int(x) for x in input().split()]

discount = (100 - p) / 100
total_cost = x
while True:
    x *= discount
    total_cost += math.floor(x)
    if math.floor(x) <= 0:
        break
print(total_cost)