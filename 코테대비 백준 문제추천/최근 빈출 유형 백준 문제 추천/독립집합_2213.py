import sys
sys.setrecursionlimit(10**9)

def dfs_makeDP(cur):
    dfs_visited[cur] = True
    dfs_dp[cur][0] = 0
    dfs_dp[cur][1] = w_list[cur]

    for nex in tree[cur]:
        if not dfs_visited[nex]:
            dfs_makeDP(nex)
            dfs_dp[cur][0] += max(dfs_dp[nex][1], dfs_dp[nex][0])
            dfs_dp[cur][1] += dfs_dp[nex][0] 

def trace(cur, pre):
    trace_visited[cur] = True

    if pre == 0:
        if dfs_dp[cur][1] > dfs_dp[cur][0]:
            trace_list.append(cur)
            for nex in tree[cur]:
                if not trace_visited[nex]:
                    trace(nex, 1)
        else:
            for nex in tree[cur]:
                if not trace_visited[nex]:
                    trace(nex, 0)
    else:
        for nex in tree[cur]:
            if not trace_visited[nex]:
                trace(nex, 0)


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    w_list = [-1] + list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    dfs_dp = [[0,0] for _ in range(n+1)]
    dfs_visited = [False] * (n+1)
    dfs_makeDP(1)

    trace_visited = [False] * (n+1)
    trace_list = []
    trace(1, 0)

    print(max(dfs_dp[1][0], dfs_dp[1][1]))
    trace_list.sort()
    print(*trace_list)