H, W, N = [int(x) for x in input().split()]

card_l = []
for i in range(H):
    card = [int(x) for x in input().split()]
    card_l.append(card)

L = int(input())

result = {"player"+str(i):0 for i in range(1,N+1)}
player = "player1"
for i in range(L):
    beat = [int(x) for x in input().split()]
    beat1 = beat[0] - 1, beat[1] - 1
    beat2 = beat[2] - 1, beat[3] - 1
    if card_l[beat1[0]][beat1[1]] == card_l[beat2[0]][beat2[1]]:
        result[player] += 2
    else:
        if player != "player" + str(N):
            player = "player" + str(int(player[-1]) + 1)
        else:
            player = "player1"

for key,value in result.items():
    print(value)