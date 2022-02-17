import sys
import heapq
import math

input = sys.stdin.readline

def distance(a, b):
    return math.sqrt(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2))

def find_parent(a):
    if a == parent[a]:
        return a
    p = find_parent(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)

    if root_a == root_b:
        return False

    if a < b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

    return True

n, m = map(int, input().split())
already = [[0]*(n+1) for _ in range(n+1)]
parent = [i for i in range(n+1)]
coordi = [0]
count = set()
q = []

for _ in range(n):
    coordi_x, coordi_y = map(int, input().split())
    coordi.append((coordi_x, coordi_y))

for _ in range(m):
    connected_a, connected_b = map(int, input().split())
    union(connected_a, connected_b)
    count.add(connected_a)
    count.add(connected_b)
    already[connected_a][connected_b] = 1
    already[connected_b][connected_a] = 1

for i in range(1, n):
    for j in range(i+1, n+1):
        if already[i][j] != 1:
            d = distance(coordi[i], coordi[j])
            heapq.heappush(q, (d, i, j))

print(q)

ans = 0
while q:
    if len(count) == n:
        break

    dist, s_node, n_node = heapq.heappop(q)

    if union(s_node, n_node):
        ans += dist
        count.add(s_node)
        count.add(n_node)

ans = round(ans, 3)
print(f'{ans:.2f}')