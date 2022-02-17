import sys
import heapq
import math
import itertools

input = sys.stdin.readline

n = int(input())
star = []
for i in range(n):
    x, y = map(float, input().split())
    star.append((x,y))

edges = []

def mst(a, b):
    return round(math.sqrt(((a[0] - b[0])**2) + ((a[1] - b[1])**2)), 2)

for j in itertools.combinations([i for i in range(n)], 2):
    heapq.heappush(edges, (mst(star[j[0]], star[j[1]]), j[0], j[1]))

edges.sort()
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

    if root_x != root_y:
        if x > y:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x

ans = 0
cnt = 1

while True:
    if cnt == n:
        break
    wei, s_node, n_node = heapq.heappop(edges)
    if find_parent(s_node) != find_parent(n_node):
        union(s_node, n_node)
        cnt += 1
        ans += wei
        
print(ans)
