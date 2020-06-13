tousen = input().split()
n = int(input())

kuji_l = []
atari_num = []
for i in range(n):
    kuji = input().split()
    atari = 0
    for j in range(len(tousen)):
        if tousen[j] in kuji:
            atari += 1
    atari_num.append(atari)
for i in atari_num:
    print(i)