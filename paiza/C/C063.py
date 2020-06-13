N = int(input())
seed_l = []
for i in range(N):
    seed = [int(x) for x in input().split()]
    seed_l.append(seed)

saku = []
for i in seed_l:
    saku.append(i[0] + i[1])
dict_saku = {x:saku.count(x) for x in saku}

max_value = 0
min_key = 999999
for key, value in dict_saku.items():
    if value >= max_value:
        if key < min_key:
            max_value = value
            min_key = key
print(min_key)