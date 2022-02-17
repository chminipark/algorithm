import collections
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
matrix = [[0] * (m) for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1

def bfs(start: tuple):
    q = collections.deque()
    q.append(start)
    cnt = 1
    matrix[start[0]][start[1]] = 0

    while q:
        cur_x, cur_y = q.popleft()
        
        for x, y in [(1,0), (-1,0), (0,-1), (0,1)]:
            nex_x = x + cur_x
            nex_y = y + cur_y
            if 0 <= nex_x < n and 0 <= nex_y < m:
                if matrix[nex_x][nex_y]:
                    q.append((nex_x, nex_y))
                    matrix[nex_x][nex_y] = 0
                    cnt += 1
    
    return cnt

ans = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            ans = max(ans, bfs((i,j)))

print(ans)
