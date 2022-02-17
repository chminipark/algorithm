import sys

input = sys.stdin.readline


def find_parent(x):
    if x == parent[x]:
        return x
    p = find_parent(parent[x])
    parent[x] = p
    return parent[x]

def union(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)

    if root_x == root_y:
        ans.append(count[root_x])
        return
    else:
        parent[root_y] = root_x
        count[root_x] += count[root_y]
        ans.append(count[root_x])
        return

ans = []
t = int(input())
for _ in range(t):
    count = dict()
    parent = dict()

    f = int(input())
    for _ in range(f):
        a, b = input().strip().split(' ')
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        union(a, b)

print(*ans, sep='\n')