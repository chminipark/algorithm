import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

inf = sys.maxsize
memo = [inf] * (v+1)
memo[k] = 0

heap = []
heapq.heappush(heap, (k, memo[k]))

while heap:
    cur_node, cur_wei = heapq.heappop(heap)

    if cur_wei > memo[cur_node]:
        continue

    for next_node, wei in graph[cur_node]:
        next_wei = cur_wei + wei
        if memo[next_node] > next_wei:
            memo[next_node] = next_wei
            heapq.heappush(heap, (next_node, next_wei))

for i in range(1, v+1):
    print('INF' if memo[i] == inf else memo[i])
