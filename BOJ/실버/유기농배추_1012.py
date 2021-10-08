import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs_stack(i,j):
    global matrix, dx, dy, m, n
    
    cnt = 1
    matrix[i][j] = 0
    stack = []
    stack.append((i,j))

    while stack:
        x, y = stack.pop()
        for a in range(4):
            nx = x+dx[a]
            ny = y+dy[a]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1:
                    stack.append((nx, ny))
                    matrix[nx][ny] = 0
                    cnt += 1
    
    return cnt

t = int(input())
count = []
answer = []
for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                count.append(dfs_stack(i,j))
    
    answer.append(len(count))
    count.clear()

for i in answer:
    print(i)