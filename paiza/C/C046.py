N = int(input())
s = {x:0 for x in input().split()}
M = int(input())

book_l = []
for i in range(M):
    book = [int(x) if str.isnumeric(x) else x for x in input().split()]
    book_l.append(book)

for i in book_l:
    if i[0] in s:
        s[i[0]] += i[1]

sort_price = []
for value in s.values():
    sort_price.append(value)
sort_price.sort(reverse=True)
ranking = []
for i in sort_price:
    for key, value in s.items():
        if value == i:
            ranking.append(key)
for i in ranking:
    print(i)