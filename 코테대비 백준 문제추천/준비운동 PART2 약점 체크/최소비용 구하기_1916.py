import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
inf = sys.maxsize
graph = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

start, end = map(int, input().split())
memo = [inf] * (n+1)
memo[start] = 0
q = []
heapq.heappush(q, (memo[start], start))

while q:
    cur_wei, cur_node = heapq.heappop(q)

    if cur_wei > memo[cur_node]:
        continue

    for next_node in range(1, n+1):
        if graph[cur_node][next_node] != inf:
            next_wei = cur_wei + graph[cur_node][next_node]
            if memo[next_node] > next_wei:
                memo[next_node] = next_wei
                heapq.heappush(q, (next_wei, next_node))

print(memo[end])