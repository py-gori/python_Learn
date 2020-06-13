X, N, M = [int(x) for x in input().split()]
C_list = []
for i in range(N):
    C = input()
    C_split = []
    for j in range(len(C)):
        C_split.append(C[j])
    C_list.append(C_split)
P_list = [] #三次元リスト
for i in range(X):
    P_tmp_list = [] #各ピース格納リスト
    for j in range(M):
        P = input()
        P_split = []
        for k in range(len(P)):
            P_split.append(P[k])
        P_tmp_list.append(P_split)
    P_list.append(P_tmp_list)

for i in range(4):
    if C_list[0][0:M-1] == P_list[0][0][0:M-1]
        if C_list[1][0:M-1] == P_list[0][1][0:M-1]:
    elif C_list[0][0] + C_list[1][0] == P_list[0][]