import sys

N, M = map(int,sys.stdin.readline().split(' '))
L=[]

for x in range(N+1):
    if x == 0:
        L.append([0]*(N+1))
    else:
        L.append([0]+list(map(int,sys.stdin.readline().split(' '))))

# print(L)

sum_L = [[0 for x in range(N + 1)] for x in range(N + 1)]

for i in range(N+1):
    for j in range(N+1):
        if i !=0 and j!=0:
            sum_L[i][j] = L[i][j] + sum_L[i-1][j] + sum_L[i][j-1] - sum_L[i-1][j-1]
# print(sum_L)

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
    base = sum_L[x2][y2]
    delta = sum_L[x1-1][y2] + sum_L[x2][y1-1] - sum_L[x1-1][y1-1]
    print(base-delta)

# 배운점
# 알고리즘 자체를 답을 모른채로 생각 못했을 듯
# 11659와 비슷하게 미리 sum을 메모리 상에 만들어두고 참고하여 사용