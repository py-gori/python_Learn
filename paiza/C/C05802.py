N, t, s = input().split()
N = int(N)

count = 0
while True:
    if t == s:
        break
    else:
        s = s[1:] + s[0]
        count += 1
print(count)