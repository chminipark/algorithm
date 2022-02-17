import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

ans = []
while q:
    cur_node = heapq.heappop(q)
    ans.append(cur_node)

    for nex in graph[cur_node]:
        indegree[nex] -= 1
        if indegree[nex] == 0:
            heapq.heappush(q, nex)

print(*ans)