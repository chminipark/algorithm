import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(m)]

def bfs(color: str, start: tuple):
    q = collections.deque()
    q.append(start)
    cnt = 1
    matrix[start[0]][start[1]] = 'O'

    while q:
        cur_x, cur_y = q.popleft()

        for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
            nex_x = x + cur_x
            nex_y = y + cur_y
            if 0 <= nex_x < m and 0 <= nex_y < n:
                if matrix[nex_x][nex_y] == color:
                    q.append((nex_x, nex_y))
                    cnt += 1
                    matrix[nex_x][nex_y] = 'O'

    return cnt

white = 0
blue = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 'W':
            white += (bfs('W', (i,j))**2)
        elif matrix[i][j] == 'B':
            blue += (bfs('B', (i,j))**2)

print(white, blue)