def appending(winner):
    second_p.append(winner)

def diff1(player1, player2):
    if t[player1-1] > t[player2-1]:
        appending(player2)
    else:
        appending(player1)

def diff2(player3, player4):
    if t[player3-1] > t[player4-1]:
        appending(player4)
    else:
        appending(player3)

p1, p2 = [int(x) for x in input().split()]
p3, p4 = [int(x) for x in input().split()]

t = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]

second_p = []
diff1(p1,p2)
diff2(p3,p4)

second_p = sorted(second_p)

if f[0] > f[1]:
    second_p = reversed(second_p)

for i in second_p:
    print(i)