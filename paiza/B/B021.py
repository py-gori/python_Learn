n = int(input())

words = []
for i in range(n):
    word = input()
    if word not in words:
        words.append(word)
new_words = []
for word in words:
    if word[-1] == "x" or word[-1] == "s" or word[-1] == "o" or word[-2:] == "ch" or word[-2:] == "sh":
        word = word + "es"
        new_words.append(word)
    elif word[-1] == "f":
        word = word.replace("f", "ves")
        new_words.append(word)
    elif word[-2:] == "fe":
        word = word.replace("fe", "ves")
        new_words.append(word)
    elif word[-1] == "y":
        if word[-2] != "a" and word[-2] != "i" and word[-2] != "u" and word[-2] != "e" and word[-2] != "o":
            word = word.replace("y", "ies")
            new_words.append(word)
        else:
            word = word + "s"
            new_words.append(word)
    else:
        word = word + "s"
        new_words.append(word)

for i in new_words:
    print(i)