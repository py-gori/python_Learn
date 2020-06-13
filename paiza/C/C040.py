N = int(input())

low_list = []
high_list = []
for i in range(N):
    diff_list = []
    c, h = [x for x in input().split()]
    if c == "le":
        low_list.append(float(h))
    else:
        high_list.append(float(h))
print(max(high_list), min(low_list))