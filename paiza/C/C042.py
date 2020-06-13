n = int(input())
shouhai_list = []

for i in range(n):
    line = ["-" for x in range(n)]
    shouhai_list.append(line)

for i in range(n * (n - 1) // 2):
    win, lose = [int(x) - 1 for x in input().split()]
    shouhai_list[win][lose] = "W"
    shouhai_list[lose][win] = "L"
for i in shouhai_list:
    kekka = " ".join(i)
    print(kekka)