N = int(input())

point = 0
for i in range(N):
    correct, word = input().split()
    if correct ==  word:
        point += 2
    elif len(correct) == len(word):
        diff = 0
        for i in range(len(word)):
            if correct[i] != word[i]:
                diff += 1
        if diff == 1:
            point += 1
print(point)