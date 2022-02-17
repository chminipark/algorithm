import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))

heap = []
inf = sys.maxsize
dist = [inf] * (V+1)

def dij(start):
    dist[start] = 0
    heapq.heappush(heap, (0,start))

    while heap:
        cur_wei, cur_node = heapq.heappop(heap)

        if dist[cur_node] < cur_wei:
            continue

        for wei, next_node in graph[cur_node]:
            next_wei = cur_wei + wei
            if dist[next_node] > next_wei:
                dist[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))

dij(K)

for i in range(1, V+1):
    print('INF' if dist[i] == inf else dist[i])
