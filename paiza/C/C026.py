N, S, p = [int(x) for x in input().split()]
carrots = []
for i in range(N):
    carrot = [int(x) for x in input().split()]
    carrots.append(carrot)

max_size = 0
carrot_num = 0
for i in range(len(carrots)):
    if carrots[i][1] >= S - p and carrots[i][1] <= S + p:
        if max_size == 0:
            max_size = carrots[i][0]
            carrot_num = i + 1
        else:
            if max_size < carrots[i][0]:
                carrot_num = i + 1
            else:
                pass
if carrot_num == 0:
    print("not found")
else:
    print(carrot_num)