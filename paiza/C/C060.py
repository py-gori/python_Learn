N, K, P = [int(x) for x in input().split()]

words = input().split()
words.sort()

p_word = []
for i in range(0, len(words), K):
    word = words[i:i+K]
    p_word.append(word)

for i in p_word[P-1]:
    print(i)