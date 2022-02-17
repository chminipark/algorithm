import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(a):
    if a == parent[a]:
        return a
    p = find_parent(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return
    else:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

ans = []
for _ in range(m):
    x, y, z = map(int, input().split())
    if x == 0:
        union(y, z)
    else:
        ans.append('YES' if find_parent(y) == find_parent(z) else 'NO')

print(*ans, sep='\n')

