import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
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

for i in range(1, n+1):
    city = [0] + list(map(int, input().split()))
    for j in range(1, n+1):
        if city[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))
check = parent[plan[0]]
for i in range(1, m):
    if check != parent[plan[i]]:
        print('NO')
        break
else:
    print('YES')