ATK, DEF, AGI = [int(x) for x in input().split()]
n = int(input())

monsters = []
for i in range(n):
    monster_l = input().split()
    monsters.append(monster_l)

evolution = []
for monster in monsters:
    if ATK >= int(monster[1]) and ATK <= int(monster[2]):
        if DEF >= int(monster[3]) and DEF <= int(monster[4]):
            if AGI >= int(monster[5]) and AGI <= int(monster[6]):
                evolution.append(monster[0])
    else:
        pass

if not evolution:
    print("no evolution")
else:
    for i in evolution:
        print(i)