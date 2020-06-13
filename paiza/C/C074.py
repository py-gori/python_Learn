H, W, X = [int(x) for x in input().split()]

word_list = []
for i in range(H):
    line = input()
    word_list.append(line)

len_word = ""
for word in word_list:
    len_word += word

after_word = []
for i in range(1,W+1):
    split_word = len_word[X*(i-1):X*i]
#    if split_word == "":
#        break
    after_word.append(split_word)

for j in after_word:
    print(j)
