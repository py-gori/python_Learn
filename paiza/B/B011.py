n, m = [int(x) for x in input().split()]

card_l = []
List_card = []
for i in range(1,100001):
    if i % n != 0:
        card_l.append(str(i))
    else:
        card_l.append(str(i))
        if len(List_card) % 2 == 0:
            List_card.append(card_l)
            card_l = []
        else:
            card_l.reverse()
            List_card.append(card_l)
            card_l = []

for i, num in enumerate(List_card):
    try:
        tmp_1 = i
        tmp_2 = (num.index(str(m)))
        break
    except ValueError:
        pass

try:
    if tmp_1 % 2 != 0:
        print(List_card[tmp_1 - 1][tmp_2])
    else:
        print(List_card[tmp_1 + 1][tmp_2])
except IndexError:
    print(List_card[tmp_1][0])
    pass
