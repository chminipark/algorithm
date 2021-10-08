## bfs

# import collections
# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [[int(i) for i in list(input().strip())] for _ in range(n)]

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# def bfs(i,j):
#     global n
#     q = collections.deque()
#     q.append((i,j))
#     graph[i][j] = 0
#     cnt = 1

#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if graph[nx][ny] == 1:
#                     q.append((nx, ny))
#                     graph[nx][ny] = 0
#                     cnt += 1
    
#     return cnt

# answer = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             answer.append(bfs(i,j))

# answer.sort()
# print(len(answer))
# for i in answer:
#     print(i)




## dfs_recursive

# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [[int(i) for i in list(input().strip())] for _ in range(n)]

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# cnt = 0
# def dfs_recur(i,j):
#     global cnt, n, graph, dx, dy
#     cnt += 1
#     graph[i][j] = 0

#     for a in range(4):
#         nx = i+dx[a]
#         ny = j+dy[a]
#         if 0 <= nx < n and 0 <= ny < n:
#             if graph[nx][ny] == 1:
#                 dfs_recur(nx, ny)

# answer = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             dfs_recur(i, j)
#             answer.append(cnt)
#             cnt = 0

# answer.sort()
# print(len(answer))
# for i in answer:
#     print(i)



## dfs_stack

import sys
input = sys.stdin.readline

n = int(input())
graph = [[int(i) for i in list(input().strip())] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs_stack(i,j):
    global graph, n, dx, dy

    cnt = 1
    graph[i][j] = 0
    stack = []
    stack.append((i,j))

    while stack:
        x, y = stack.pop()
        for a in range(4):
            nx = x+dx[a]
            ny = y+dy[a]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    stack.append((nx,ny))
                    cnt += 1
                    graph[nx][ny] = 0
    
    return cnt

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(dfs_stack(i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)

