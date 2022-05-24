import heapq


V, E = map(int, input().split())
start = int(input())

node = [[]for _ in range(V+1)]
pq = []
value_table = [float("INF")] * (V+1)
value_table[start] = 0
heapq.heappush(pq, (0,start))

for _ in range(E):
    u,v,w = map(int,input().split())
    node[u].append((v,w))
print(node)

# print(pq)

while pq:
    print(pq)
    w,n = heapq.heappop(pq)
    if value_table[n] < w:
        continue
    for goal, value in node[n]:
        if value_table[goal] > w + value:
            value_table[goal] = w + value
            heapq.heappush(pq, (w + value, goal))


# print(pq)