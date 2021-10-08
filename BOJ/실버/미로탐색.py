import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [[int(i) for i in list(input().strip())] for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

q = collections.deque()
q.append((0,0))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))

print(maze[n-1][m-1])
