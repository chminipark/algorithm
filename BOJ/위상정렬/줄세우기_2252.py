import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = collections.deque()
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    node = q.popleft()
    result.append(node)

    for nex in graph[node]:
        indegree[nex] -= 1
        if indegree[nex] == 0:
            q.append(nex)
    
print(*result)