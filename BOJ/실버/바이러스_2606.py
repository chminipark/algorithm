import sys
input = sys.stdin.readline

node = int(input())
line = int(input())

graph = [[0]*(node+1) for _ in range(node+1)]

for _ in range(line):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

ans = 0
def dfs(start_node, visited = []):
    global ans
    visited.append(start_node)

    for i in range(len(graph[start_node])):
        if graph[start_node][i] == 1 and i not in visited:
            dfs(i, visited)
            ans += 1

dfs(1)
print(ans)