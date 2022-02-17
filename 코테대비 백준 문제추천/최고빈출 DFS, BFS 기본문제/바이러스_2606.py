import sys

input = sys.stdin.readline

com_cnt = int(input())
edge_cnt = int(input())
graph = [[] for _ in range(com_cnt+1)]
for _ in range(edge_cnt):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs_stack():
    stack = []
    stack.append(1)
    cnt = 0
    visited = [False] * (com_cnt+1)
    visited[1] = True

    while stack:
        cur = stack.pop()

        for nex in graph[cur]:
            if not visited[nex]:
                stack.append(nex)
                cnt += 1
                visited[nex] = True

    return cnt

print(dfs_stack())