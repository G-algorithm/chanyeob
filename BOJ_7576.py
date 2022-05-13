from collections import deque
from pprint import pprint

M, N = map(int,input().split())

Warehouse = []
for _ in range(N) :
    Warehouse.append(list(map(int,input().split())))

# print(Warehouse)

direction_x = [-1,1,0,0]
direction_y = [0,0,-1,1]

queue = deque()
empty = 0

for i in range (N):
    for j in range (M):
        if Warehouse[i][j] == 1:
            queue.append([i,j])
        elif Warehouse[i][j] == -1:
            empty += 1

turn = 0

while True:
    if len(queue) == 0 :
        break
    for _ in range (len(queue)):
        current = queue.popleft()
        x = current[0]
        y = current[1]

        for i in range (4):
            nx = x+direction_x[i]
            ny = y+direction_y[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if Warehouse[nx][ny] == 0:
                    Warehouse[nx][ny] = 1
                    queue.append([nx,ny])
    # print()
    # pprint(Warehouse)
    turn += 1

wrong = 0

for i in range (N):
    for j in range(M):
        if Warehouse[i][j] == 0:
            wrong += 1

if wrong == 0 :
    print(turn-1)
else:
    print(-1)