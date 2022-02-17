import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

parent = [i for i in range(n)]

def find_parent(x):
    if x == parent[x]:
        return x
    p = find_parent(parent[x])
    parent[x] = p
    return parent[x]

def union(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)

    if x < y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

union(edges[0][0], edges[0][1])
for i in range(1, m):
    if find_parent(edges[i][0]) == find_parent(edges[i][1]):
        print(i+1)
        break
    union(edges[i][0], edges[i][1])
else:
    print(0)