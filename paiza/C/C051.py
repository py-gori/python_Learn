num = input().split()

X = []
for i in range(4):
    x = int(num[0] + num[1]) + int(num[2] + num[3])
    x2 = int(num[0] + num[2]) + int(num[1] + num[3])
    x3 = int(num[0] + num[3]) + int(num[1] + num[2])
    X.append(x)
    X.append(x2)
    X.append(x3)
    tmp = num.pop()
    num.insert(0, tmp)
print(max(X))