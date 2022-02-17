# ### BFS ###

# import sys
# import collections

# input = sys.stdin.readline

# n = int(input())
# matrix = [list(input().strip()) for _ in range(n)]
# dxdy = [(1,0), (0,1), (-1,0), (0,-1)]

# def bfs(a, b):
#     q = collections.deque()
#     q.append((a,b))
#     matrix[a][b] = '0'
#     cnt = 0

#     while q:
#         x, y = q.popleft()
#         cnt += 1
#         for dx, dy in dxdy:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < n and 0 <= ny < n:
#                 if matrix[nx][ny] == '1':
#                     q.append((nx, ny))
#                     matrix[nx][ny] = '0'
                    
    
#     return cnt

# ans = []
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] == '1':
#             ans.append(bfs(i,j))

# ans.sort()
# print(len(ans))
# for i in ans:
#     print(i)


# ### DFS(Stack) ###

# import sys

# input = sys.stdin.readline

# n = int(input())
# matrix = [list(input().strip()) for _ in range(n)]
# dxdy = [(1,0), (0,1), (-1,0), (0,-1)]

# def DFS_Stack(a,b):
#     matrix[a][b] = '0'
#     stack = [(a,b)]
#     cnt = 0

#     while stack:
#         x, y = stack.pop()
#         cnt += 1

#         for dx, dy in dxdy:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < n and 0 <= ny < n:
#                 if matrix[nx][ny] == '1':
#                     stack.append((nx, ny))
#                     matrix[nx][ny] = '0'
    
#     return cnt


# ans = []
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] == '1':
#             ans.append(DFS_Stack(i,j))

# ans.sort()
# print(len(ans))

# for i in ans:
#     print(i)



### DFS_recur ###

import sys

input = sys.stdin.readline

n = int(input())
matrix = [list(input().strip()) for _ in range(n)]
dxdy = [(1,0), (0,1), (-1,0), (0,-1)]

def DFS_recur(x,y):
    global cnt

    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if matrix[nx][ny] == '1':
                matrix[nx][ny] = '0'
                cnt += 1
                DFS_recur(nx, ny)
    else:
        return

ans = []
cnt = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1':
            matrix[i][j] = '0'
            cnt = 1
            DFS_recur(i,j)
            ans.append(cnt)
            cnt = 0

ans.sort()
print(len(ans))
for i in ans:
    print(i)