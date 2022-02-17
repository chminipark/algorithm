import collections
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs_stack():
    stack = [v]
    ans = []
    visited = [0] * (n+1)

    while stack:
        cur = stack.pop()
        if visited[cur]: continue
        ans.append(cur)
        visited[cur] = 1

        if len(ans) == n:
            break
        
        for nex in reversed(sorted(graph[cur])):
            if not visited[nex]:
                stack.append(nex)

    return ans

def bfs_queue():
    q = collections.deque([v])
    ans = []
    visited = [0] * (n+1)

    while q:
        cur = q.popleft()
        if visited[cur]:
            continue

        ans.append(cur)
        visited[cur] = 1

        if len(ans) == n:
            break

        for nex in sorted(graph[cur]):
            if not visited[nex]:
                q.append(nex)

    return ans


def dfs_recur(cur_node):

    recur_visited = [0] * (n+1)
    recur_visited[v] = 1
    recur_ans = []

    def recursive(cur_node):

        if len(recur_ans) == n:
            return
        recur_ans.append(cur_node)
        recur_visited[cur_node] = 1
        
        for nex in sorted(graph[cur_node]):
            if not recur_visited[nex]:
                recursive(nex)

    recursive(cur_node)

    return recur_ans


# print(*dfs_stack())
print(*dfs_recur(v))
print(*bfs_queue())
