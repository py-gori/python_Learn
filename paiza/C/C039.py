E = [x for x in input().split("+")]

num_list = []
for i in E:
    ju = 0
    ichi = 0
    for j in range(len(i)):
        if i[j] == "<":
            ju += 1
        elif i[j] == "/":
            ichi += 1
    num = str(ju) + str(ichi)
    num_list.append(num)

numbers = [int(x) for x in num_list]
result_sum = 0
for i in numbers:
    result_sum += i
print(result_sum)