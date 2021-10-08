import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    temp = list(map(int, input().split()))
    if len(temp) <= 2:
        continue
    node = temp[0]
    temp = temp[1:-1]
    for i in range(0,len(temp),2):
        tree[node].append((temp[i],temp[i+1]))


def max_nl(node):
    visited = [0]*(v+1)
    max_l = 0
    max_n = 0
    visited[node] = 1
    def dfs(node):
        nonlocal max_l, max_n
        for n,l in tree[node]:
            if visited[n] == 0:
                visited[n] = visited[node] + l
                if max_l < visited[n]:
                    max_l = visited[n]
                    max_n = n
                dfs(n)
    dfs(node)
    return max_n, max_l-1

y, max_yline = max_nl(1)
ans = max_nl(y)
print(ans[1])