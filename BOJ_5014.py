from collections import deque

F,S,G,U,D = map(int,input().split())

# F : 건물의 총 층수
# S : 현재 층 # 1
# G : 스타트링크 있는 층 # 5
# U : 위로 U번 가는 버튼 # 3
# D : 아래로 D번 가는 버튼 # 2
# 5 1 5 3 2
# 10 2 10 3 1 << 이걸로 설명
# 갈 수 없다면 "use the stairs"

#BFS

queue = deque([S])
visited = [-1] * (F+1)
visited[S] = 0
while queue:
    # print(queue)
    current = queue.popleft()
    # print("current:",current)
    if current != G:
        for next_step in (current+U, current-D): # up or down
            if 1 <= next_step <= F and visited[next_step] == -1: # next step 통합으로
                visited[next_step] = visited[current] + 1
                queue.append(next_step) # queue에는 up이든 down이든 갈 수 있는 후보들이 저장됨
    else:
        break
        # print(visited)
    # print(queue) # queue : 갈 수 있는 후보들의 체킹 순서를 기억한다.

# print(visited) # 방문했는지 여부를 기억함과 동시에 각 위치까지 갈 수 있는 최소 경로를 저장한다.
if visited[G] != -1: # 끝까지 도달했다면 정상 출력
    print(visited[G])
else: # 끝까지 도달하지 못했으면 계단쓰세요~
    print("use the stairs")