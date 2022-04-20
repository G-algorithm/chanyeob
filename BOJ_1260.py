'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
from collections import defaultdict, deque

N,M,V = input().split()
N,M,V = int(N),int(M),int(V)

# print(N,M,V)

graph = defaultdict(list)
for _ in range (M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in graph:
    graph[x].sort()

# print(graph)
visited = set()

def DFS(graph, v, visited): # 1
    # print(v)
    if v not in visited:
        print(v,end=" ")
        visited.add(v)
    for i in (graph[v]): # graph[1] = [2,3,4]
        # print(i)
        if i not in visited:
            # print(i)
            DFS(graph, i,visited)


def BFS(graph, v, visited):
    queue = deque([v])
    visited.add(v)
    while queue:
        current = queue.popleft()
        print(current,end= " ")
        # print(visited)
        for i in (graph[current]):
            if i not in visited:
                queue.append(i)
                visited.add(i)


# print(graph)
DFS(graph, V, visited)
print()
visited=set()
BFS(graph, V, visited)