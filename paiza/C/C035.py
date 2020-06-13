N = int(input())

gokaku = 0
for i in range(N):
    data = input().split()
    score = data[1:]
    score = [int(x) for x in score]
    sum_score = sum(score)
    if sum_score >= 350:
        if data[0] == "s":
            if score[1] + score[2] >= 160:
                gokaku += 1
        elif data[0] == "l":
            if score[3] + score[4] >= 160:
                gokaku += 1
print(gokaku)