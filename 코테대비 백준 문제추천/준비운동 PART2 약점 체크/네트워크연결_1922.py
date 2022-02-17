####################
### 크루스칼 알고리즘 ###
####################

# import sys

# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# edges = []
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     edges.append((c, a, b))
# edges.sort()

# parent = [0] * (n+1)
# for i in range(1, n+1):
#     parent[i] = i

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)

#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# ans = 0
# for e in edges:
#     cost, s_node, n_node = e

#     if find_parent(parent, s_node) != find_parent(parent, n_node):
#         union(parent, s_node, n_node)
#         ans += cost

# print(ans)



####################
#### 프림 알고리즘 ####
####################


# import sys
# import heapq

# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# graph = [[]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((c, b))
#     graph[b].append((c, a))

# def prim(start):
#     visited = [0] * (n+1)
#     heap = [(0, start)]
#     cnt = 0
#     ans = 0

#     while cnt < n:
#         wei, node = heapq.heappop(heap)

#         if visited[node]: continue
#         visited[node] = 1
#         cnt += 1
#         ans += wei
#         for next_wei, next_node in graph[node]:
#             heapq.heappush(heap, (next_wei, next_node))
    
#     return ans

# print(prim(1))


####################
### 크루스칼 알고리즘 ###
####################

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
m = int(input())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
cnt = 0

for cost, s_node, n_node in edges:
    if cnt == n:
        break
    if find_parent(s_node) != find_parent(n_node):
        ans += cost
        cnt += 1
        union(s_node, n_node)

print(ans)