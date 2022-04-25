'''
5 3
5 4 3 2 1
1 3
2 4
5 5
'''
import sys

N, M = map(int,sys.stdin.readline().split(' '))
L = list(map(int,sys.stdin.readline().split(' ')))
cnt = 0
answer = [0]

for i in range(len(L)):
    cnt += L[i]
    answer.append(cnt)

for _ in range(M):
    i,j = map(int, sys.stdin.readline().split(' '))
    print(answer[j] - answer[i-1])

# -배운점-
# sys.stdin.readline()을 쓰자
# 처음에는 sum, slice를 써서 해결하려했는데 DP처럼 활용해서 더 시간적 효율을 냈다. (15~17,21번째줄)