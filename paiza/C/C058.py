N, t, s = input().split()
N = int(N)

count = 0
while True:
    if t == s:
        break
    s = s[1:len(s)] + s[0]
    count += 1
print(count)