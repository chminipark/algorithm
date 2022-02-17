import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
vill = [0] + list(map(int, input().split()))
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

dp = [[0,0] for _ in range(n+1)]
dfs_visited = [False] * (n+1)
def dfs_dp(cur):
    dfs_visited[cur] = True
    dp[cur][0] = 0
    dp[cur][1] = vill[cur]

    for nex in edges[cur]:
        if not dfs_visited[nex]:
            dfs_dp(nex)
            dp[cur][0] += max(dp[nex][1], dp[nex][0])
            dp[cur][1] += dp[nex][0]

dfs_dp(1)
print(max(dp[1][0], dp[1][1]))