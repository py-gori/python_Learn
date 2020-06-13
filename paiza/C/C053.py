N = int(input())
card = [int(x) if x != "x10" else "x10" for x in input().split()]

if 0 in card:
    max_n = 0
    for i in card:
        if i != "x10":
            if max_n < i:
                max_n = i
    max_index = card.index(max_n)
    card[max_index] = 0

sum_card = 0
for i in card:
    if i != "x10":
        sum_card += i
if "x10" in card:
    sum_card *= 10

print(sum_card)