import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

check = [False] * (n+1)
result = []
dp = [[0,0] for _ in range(n+1)]

def dfs(cur):
    check[cur] = True
    dp[cur][1] = 1

    for nex in tree[cur]:
        if not check[nex]:
            dfs(nex)
            dp[cur][0] += max(dp[nex][0], dp[nex][1])
            dp[cur][1] += dp[nex][0]

dfs(1)
print(n - max(dp[1][0], dp[1][1]))