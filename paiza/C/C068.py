N = int(input())
S = input()
S = list(S)

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = ""
for i in range(1,len(S)+1):
    if i % 2 != 0:
        tmp_index = A.index(S[i-1]) - N
        answer += A[tmp_index]
    else:
        tmp_index = A.index(S[i-1]) + N
        if tmp_index > len(A) - 1:
            tmp_index = tmp_index - len(A)
            answer += A[tmp_index]
        else:
            answer += A[tmp_index]
print(answer)
