from collections import defaultdict, deque

N = int(input())

L = defaultdict(list)

for _ in range (N-1):
    a,b = map(int,input().split(' '))
    L[a].append(b)
    L[b].append(a)

print(L)

queue = deque()
queue.append(1) # 1번에서 시작할 것

ans = [0]*(N+1) # 0~N번까지 노드들의 부모노드를 저장하는 리스트

def bfs():
    while queue:
        now = queue.popleft() # 1
        for nxt in L[now]: # L[1] : 6,4
            if ans[nxt] == 0: # ans[6], ans[4]
                ans[nxt] = now # ans[6] = 1, ans[4] = 1
                queue.append(nxt) # queue = [6,4]

bfs()
print(ans)
for x in ans[2:]: # 0,1은 부모노드가 없다. 그래서 2:로 시작
    print(x)