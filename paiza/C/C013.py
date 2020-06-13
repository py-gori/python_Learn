n = input()
m = int(input())
hope = []
for i in range(m):
    room = input()
    for j in n:
        if j not in room:
            hope.append(room)
        else:
            pass
if not hope:
    print("none")
else:
    for i in hope:
        print(i)
