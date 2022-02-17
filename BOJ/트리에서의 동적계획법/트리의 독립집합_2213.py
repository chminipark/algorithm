import sys

input = sys.stdin.readline

n = int(input())
w_list = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


dp = [[0,0] for _ in range(n+1)]
dfs_visited = [False] * (n+1) 
def dfs(cur):
    dfs_visited[cur] = True
    dp[cur][0] = 0
    dp[cur][1] = w_list[cur]

    for nex in tree[cur]:
        if not dfs_visited[nex]:
            dfs(nex)
            dp[cur][0] += max(dp[nex][0], dp[nex][1])
            dp[cur][1] += dp[nex][0]

trace_visited = [False] * (n+1)
trace_list = []
def trace(cur, pre):
    trace_visited[cur] = True

    if pre == 1:
        for nex in tree[cur]:
            if not trace_visited[nex]:
                trace(nex, 0)
    else:
        if dp[cur][0] > dp[cur][1]:
            for nex in tree[cur]:
                if not trace_visited[nex]:
                    trace(nex, 0)
        else:
            trace_list.append(cur)
            for nex in tree[cur]:
                if not trace_visited[nex]:
                    trace(nex, 1)

dfs(1)
trace(1, 0)
trace_list.sort()
print(max(dp[1][0], dp[1][1]))
print(*trace_list)