m, p, q = [int(x) for x in input().split()]

x = m - (m * (p / 100))
y = x - (x * (q / 100))
print(y)