# import sys

# input = sys.stdin.readline

# m, n = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(m)]
# dp = [[-1] * n for _ in range(m)]

# stack = [(0,0)]

# dp[0][0] = 1
# while stack:
#     to_i, to_j = stack.pop()
#     for d in [[0,1],[1,0],[-1,0],[0,-1]]:
#         to_move_i = to_i + d[0]
#         to_move_j = to_j + d[1]
#         if 0 <= to_move_i < m and 0 <= to_move_j < n:
#             if matrix[to_i][to_j] > matrix[to_move_i][to_move_j]:
#                 dp[to_move_i][to_move_j] += 1
#                 stack.append((to_move_i, to_move_j))

# print(dp[-1][-1])

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(m)]

check = [[-1]*n for _ in range(m)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def dfs_recur(y,x):
    if y == m-1 and x == n-1:
        return 1
    if check[y][x] != -1:
        return check[y][x]

    check[y][x] = 0

    for i in range(4):
        to_y = y + dy[i]
        to_x = x + dx[i]

        if 0 <= to_y < m and 0 <= to_x < n:
            if mapp[to_y][to_x] < mapp[y][x]:
                check[y][x] += dfs_recur(to_y, to_x)

    return check[y][x]

print(dfs_recur(0,0))