import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

inf = sys.maxsize
bus = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a][b] = min(bus[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                bus[i][j] = 0
                continue
            bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])

for row in bus[1:]:
    for cost in row[1:]:
        print(0 if cost == inf else cost, end=' ')
    print()