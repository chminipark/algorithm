# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# n = int(input())

# tree = [[] for _ in range(n+1)]
# parent = [0]*(n+1)
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     tree[a].append(b)
#     tree[b].append(a)

# def dfs(node):
#     for i in tree[node]:
#         if parent[i] == 0:
#             parent[i] = node
#             dfs(i)

# dfs(1)

# for i in range(2,len(parent)):
#     print(parent[i])

import sys
import collections
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
parent = [0]*(n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = collections.deque()
q.append(1)

while q:
    node = q.popleft()
    for i in tree[node]:
        if parent[i] == 0:
            parent[i] = node
            q.append(i)

for i in range(2, len(parent)):
    print(parent[i])
