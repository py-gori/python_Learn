test_list = []
for i in range(7):
    test = []
    for j in range(10):
        test.append(".")
    test_list.append(test)

H, W, X = [int(x) for x in input().split()]
for i in range(7):
    for j in range(10):
        if "#" not in test_list[0][X:W+1]:
            for t in range(W):
                test_list[i][X + t] = "#"
            break
        break

if "#" not in test_list[4][5:1]:
    print("True")
else:
    print("False")
'''
for i in test_list:
    print(*i)
'''