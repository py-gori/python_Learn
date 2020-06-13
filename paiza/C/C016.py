input_line = input()
L = list(input_line)
N = len(L)

for i in range(N):
    if "A" == L[i]:
        L[i] = "4"
    if "E" == L[i]:
        L[i] = "3"
    if "G" == L[i]:
        L[i] = "6"
    if "I" == L[i]:
        L[i] = "1"
    if "O" == L[i]:
        L[i] = "0"
    if "S" == L[i]:
        L[i] = "5"
    if "Z" == L[i]:
        L[i] = "2"

for i in L:
    print(i, end ="")
print("")
