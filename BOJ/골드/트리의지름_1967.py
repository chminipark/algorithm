import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

v = int(input())
if v == 1:
    print(0)
    sys.exit(0)
tree = [[] for _ in range(v+1)]
for _ in range(v-1):
    parent, child, line = map(int, input().split())
    tree[parent].append((child, line))
    tree[child].append((parent, line))

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