n, x = [int(x) for x in input().split()]

bin_2 = 0
while True:
    if x == 0:
        break
    amari = x % 2
    x = x // 2
    if bin_2 == 0:
        bin_2 = str(amari)
    else:
        bin_2 = str(amari) + bin_2

X = []
for i in range(n):
    pop_n = int(input())
    x = bin_2[-pop_n]
    X.append(x)

for i in X:
    print(i)