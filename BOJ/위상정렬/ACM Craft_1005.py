import collections
import sys

input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    n, k = map(int, input().split())
    time = [-1] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    goal = int(input())

    dp = [0] * (n+1)
    q = collections.deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]


    while q:
        cur_node = q.popleft()

        for nex in graph[cur_node]:
            indegree[nex] -= 1
            dp[nex] = max(dp[nex], dp[cur_node] + time[nex])
            if indegree[nex] == 0:
                q.append(nex)

    ans.append(dp[goal])

print(*ans)
