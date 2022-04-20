'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

# def BFS(view, start, visited):

from pprint import pprint

N = input()
view = []
visited = []
for _ in range (int(N)):
    view.append(list(map(int,input())))
    visited.append([0]*int(N))

cnt = 0

def DFS(view,i,j,visited,count):
    visited[i][j] = 1
    if view[i][j] != 0 and j>=0 and i >=0:
        print(i,j)
        view[i][j] = 5
        #상하좌우
        if i-1 <= 0:
            if visited[i-1][j] == 0:
                DFS(view,i-1,j,visited,count)
        if i+1 < int(N): # 맵을 벗어나지 않는 경우
            if visited[i+1][j] == 0: # 방문하지 않았을 경우
                DFS(view,i+1,j,visited,count) # DFS(하)
        if j+1 < int(N):
            if visited[i][j+1] == 0:
                DFS(view,i,j+1,visited,count)
        if j-1 <= 0:
            if visited[i][j-1] == 0:
                DFS(view,i,j-1,visited,count)


for i in range(int(N)):
    for j in range(int(N)):
        if visited[i][j] == 0:
            visited[i][j] = 1 # visited 0이면 1로 만들면서 탐색
            if view[i][j] == 1:
                cnt+=1
                DFS(view,i,j,visited,1)
                print("--")
        # view를 탐색한다. visited가 0이면 탐색
        # view를 탐색하면서 0이 아니면 DFS 실행
        # DFS 끝나고나서
pprint(view)
print('----')
pprint(visited)
