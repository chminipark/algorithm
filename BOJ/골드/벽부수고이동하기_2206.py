import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[int(i) for i in list(input().strip())] for _ in range(n)]
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
q = collections.deque()
q.append((0,0,1))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q:
    x, y, w = q.popleft()
    if x == n-1 and y == m-1:
        print(visit[x][y][w]+1)
        sys.exit(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 0 and visit[nx][ny][w] == 0:
                visit[nx][ny][w] = visit[x][y][w] + 1
                q.append((nx,ny,w))
            elif matrix[nx][ny] == 1 and w == 1:
                visit[nx][ny][0] = visit[x][y][w] + 1
                q.append((nx,ny,0))

print(-1)