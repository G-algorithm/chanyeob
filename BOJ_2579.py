"""
DP 응용 1
"""

n = int(input())
step = []
for x in range(n):
    step.append(int(input()))
# print(step)

DP = [0 for x in range (n)]
for i in range(n):
    if i == 0:
        DP[i] = step[i]
    elif i == 1:
        DP[i] = step[i] + step[i-1]
    elif i == 2:
        DP[i] = max(step[i-1]+step[i], step[i-2]+step[i])
    else:
        # DP[i] = max(DP[i-3]+step[i-2]+step[i],DP[i-3]+step[i-1]+step[i])
        DP[i] = max(DP[i-2]+step[i],DP[i-3]+step[i-1]+step[i])

print(DP[-1])