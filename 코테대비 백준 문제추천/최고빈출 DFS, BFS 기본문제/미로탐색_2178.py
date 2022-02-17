import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(n)]
q = collections.deque()
q.append((0,0))
maze[n-1][m-1] = sys.maxsize

while q:
    cur_x, cur_y = q.popleft()

    for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
        nex_x = cur_x + x
        nex_y = cur_y + y

        if 0 <= nex_x < n and 0 <= nex_y < m:
            if maze[nex_x][nex_y] == 0:
                continue
            if nex_x == n-1 and nex_y == m-1:
                maze[nex_x][nex_y] = min(maze[nex_x][nex_y], maze[cur_x][cur_y] + 1)
                continue
            if maze[nex_x][nex_y] == 1:
                q.append((nex_x, nex_y))
                maze[nex_x][nex_y] = maze[cur_x][cur_y] + 1

print(maze[n-1][m-1])