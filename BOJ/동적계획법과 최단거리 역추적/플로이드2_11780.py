import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

memo = [[0]*(n+1) for _ in range(n+1)]
for k in range()
for i in range(1):
    for j in range(1, n+1):
        if i == j:
            continue
        memo[i][j] = max(graph[])
