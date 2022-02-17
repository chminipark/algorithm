# import sys
# import heapq

# input = sys.stdin.readline

# v, e = map(int, input().split())
# graph = [[] * (v+1) for _ in range(v+1)]
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))
#     # graph[a] = (b,c)
#     # graph[b] = (a,c) 

# def prim(start):
#     visited = [0] * (v+1)
#     # visited[start] = 1
#     heap = [(0, start)]
#     # for n, w in graph[start]:
#     #     heapq.heappush(heap, (w, n))
#     cnt = 0
#     ans = 0

#     while cnt < v:
#         wei, node = heapq.heappop(heap)
#         if visited[node]:
#             continue
#         visited[node] = 1
#         cnt += 1
#         ans += wei
#         for n, w in graph[node]:
#             heapq.heappush(heap, (w, n))
    
#     return ans

# print(prim(1))




#### 프림 알고리즘 #####

# import sys
# import heapq

# input = sys.stdin.readline

# v, e = map(int, input().split())
# graph = [[]*(v+1) for _ in range(v+1)]
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph[a].append((c,b))
#     graph[b].append((c,a))

# heap = [(0,1)]
# cnt = 0
# ans = 0
# visited = [0] * (v+1)

# while cnt < v:
#     wei, node = heapq.heappop(heap)

#     if visited[node]: continue
#     visited[node] = 1
#     cnt += 1
#     ans += wei
#     for next_wei, next_node in graph[node]:
#         heapq.heappush(heap, (next_wei, next_node))

# print(ans)



#### 크루스칼 알고리즘 ####
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

parent = [0] * (v+1)
for i in range(v+1):
    parent[i] = i

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b :
        parent[b] = a
    else:
        parent[a] = b

ans = 0
cnt = 0
for cost, s_node, n_node in edges:
    if cnt == v: break
    if find_parent(s_node) != find_parent(n_node):
        union(s_node, n_node)
        cnt += 1
        ans += cost

print(ans)