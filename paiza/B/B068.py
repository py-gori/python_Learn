n, h, w, k = [int(x) for x in input().split()]
total = 1

if n == h and n == w:
    yoko = 2
elif n == h or n == w:
    yoko = 3
else:
    yoko = 4

move_h1 = n - h
move_h2 = n - 1 - move_h1
move_h = [move_h1, move_h2]
move_w1 = n - w
move_w2 = n - 1 - move_w1
move_w = [move_w1, move_w2]

if n == h and n == w:
    naname = max(move_h)
elif n == h or n == w:
    naname = min(move_h) + max(move_h)
else:
    naname = (min(move_h) * 2) + min(move_w) + max(move_w)
total += yoko + naname
print(total)