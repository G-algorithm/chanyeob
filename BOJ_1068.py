N = int(input())
tree = list(map(int,input().split()))
d = int(input())

def dfs(d, tree):
    tree[d] = -2
    for i in range(len(tree)):
        if tree[i] == d:
            dfs(i,tree)

dfs(d,tree)

# print(tree)
count = 0
for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        count += 1

print(count)