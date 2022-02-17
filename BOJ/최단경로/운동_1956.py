import sys
import math

input = sys.stdin.readline

v, e = map(int, input().split())
cost = [[math.inf] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    cost[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

answer = math.inf
for i in range(1,v+1):
    answer = min(answer, cost[i][i])

print(-1 if answer == math.inf else answer)