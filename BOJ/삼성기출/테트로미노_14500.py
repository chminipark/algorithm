# import sys
# input = sys.stdin.readline
# import collections
# import copy

# n, m = map(int, input().split())
# paper = [list(map(int, input().split())) for _ in range(n)]
# answer = float('-inf')

# def bfs(current):
#     q = collections.deque()
#     q.append({current})
#     visited = []
#     added = []
#     ans = 0
#     while q:
#         tet = q.popleft()
#         for i in tet:
#             for j in [[0,1],[0,-1],[1,0],[-1,0]]:
#                 if 0 <= i[0]+j[0] < n and 0 <= i[1]+j[1] < m:
#                     n_tet = copy.deepcopy(tet)
#                     n_tet.add((i[0]+j[0], i[1]+j[1]))
#                     if len(n_tet) == 4 and n_tet not in visited:
#                         visited.append(n_tet)
#                         temp = 0
#                         for t in n_tet:
#                             temp += paper[t[0]][t[1]]
#                         ans = max(ans, temp)
#                         continue
#                     elif len(n_tet) == 4:
#                         continue
#                     elif n_tet not in q and n_tet not in added:
#                         q.append(n_tet)
#                         added.append(n_tet)           
#     return ans

# for i in range(n):
#     for j in range(m):
#         answer = max(answer, bfs((i,j)))
# print(answer)

## 시간초과....

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

stack = []
answer = float('-inf')
visited = []
def dfs(current):
    if not (0 < current[0] <= n and 0 < current[1] <= m):
        return
    if len(stack) == 4:
        temp = 0
        for i in stack:
            temp += paper[i[0]][i[1]]
        answer = max(answer, temp)
        return
    for i in [[0,1], [0,-1], [1,0], [-1,0]]:
