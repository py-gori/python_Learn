A, B = input().split()

if len(A) < len(B):
    A = A.zfill(len(B))
elif len(A) > len(B):
    B = B.zfill(len(A))

answer = []
for i in range(len(A)):
    a_1 = int(A[i]) + int(B[i])
    a_1 = str(a_1)
    answer.append(a_1[-1])

answer = "".join(answer)
print(answer)