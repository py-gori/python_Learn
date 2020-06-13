N = int(input())

result = []
ball_c = 0
strike_c = 0
for i in range(N):
    throw = input()
    result.append(throw)

judge = result

ball_c = 0
strike_c = 0
for i in range(N):
    if judge[i] == "ball":
        judge[i] = "ball!"
        ball_c += 1
        if ball_c == 4:
            judge[i] = "fourball!"
    elif judge[i] == "strike":
        judge[i] = "strike!"
        strike_c += 1
        if strike_c == 3:
            judge[i] = "out!"

for i in range(N):
    print(judge[i])
