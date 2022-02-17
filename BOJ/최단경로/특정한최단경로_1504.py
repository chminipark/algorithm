import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1, v2 = map(int, input().split())
inf = sys.maxsize

def dij(start):

    dist = [inf] * (n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cur_wei, cur_node = heapq.heappop(heap)

        if dist[cur_node] < cur_wei:
            continue

        for wei, next_node in graph[cur_node]:
            next_wei = wei + cur_wei
            if dist[next_node] > next_wei:
                dist[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
    
    return dist

dij_one = dij(1)
dij_v1 = dij(v1)
dij_v2 = dij(v2)

answer = min((dij_one[v1] + dij_v1[v2] + dij_v2[n]), (dij_one[v2] + dij_v2[v1] + dij_v1[n]))
print(-1 if answer >= inf else answer)
