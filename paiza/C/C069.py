y, m, d = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]

x_year = y
if m % 2 == 0:
    x_day = 15 - d
else:
    x_day = 13 - d

while True:
    if m == a:
        break
    else:
        m += 1
        if m == 14:
            m = 1
            x_year += 1
        if m % 2 == 0:
            x_day += 15
        else:
            x_day += 13
if a % 2 == 0:
    x_day -= 15 - b
else:
    x_day -= 13 - b

year_day = (15 * 6) + (13 * 7)
while True:
    if x_year % 4 == 1:
        print(x_day)
        break
    else:
        x_day += year_day
        x_year += 1