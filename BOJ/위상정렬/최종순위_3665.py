import sys
import collections

input = sys.stdin.readline

ans = []
t = int(input())
for _ in range(t):
    n = int(input())
    last_n = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for idx, node in enumerate(last_n):
        graph[node] = last_n[idx+1:n]
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
        else:
            graph[b].remove(a)
            graph[a].append(b)
    indegrees = [0] * (n+1)
    for edges in graph:
        for i in edges:
            indegrees[i] += 1

    q = collections.deque()
    for i in range(1, n+1):
        if indegrees[i] == 0:
            q.append(i)

    result = []
    while True:
        if len(result) == n:
            break
        if len(q) >= 2:
            result.append('?')
            break
        if not q:
            result.append('IMPOSSIBLE')
            break
        
        cur_node = q.popleft()
        result.append(cur_node)
        for nex in graph[cur_node]:
            indegrees[nex] -= 1
            if indegrees[nex] == 0:
                q.append(nex)
    
    if result[-1] == '?':
        ans.append('?')
    elif result[-1] == 'IMPOSSIBLE':
        ans.append('IMPOSSIBLE')
    elif len(result) == n:
        ans.append(result)

for i in ans:
    if type(i) == str:
        print(i)
    else:
        print(*i)
        
        