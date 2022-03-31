"""
DP 기초
"""

n = int(input())

# DP = [0 for x in range (n+1)] # [0,0,0,0,0,0,0,0,0,0,0]

DP = [0 for x in range(n+1)]

DP2 = [[0]*2]*5

print(DP2)

# 0, 1, 1, 2, 3, 5, 8, ...
for i in range (n+1):
    if i == 0:
        DP[i] = 0
    elif i == 1 :
        DP[i] = 1
    else:
        DP[i] = DP[i-1] + DP[i-2] # i==2, DP[10] = DP[9] + DP[8]
        # print(DP)

print(DP[-1])