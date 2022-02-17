import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def bfs(i,j):
    q = collections.deque()
    q.append((i, j, 0))
    visited = [[False] * (m) for _ in range(n)]
    visited[i][j] = True

    while q:
        cur_x, cur_y, cur_cnt = q.popleft()
        for x, y in [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
            nex_x = x + cur_x
            nex_y = y + cur_y
            if 0 <= nex_x < n and 0 <= nex_y < m:
                if matrix[nex_x][nex_y]:
                    return cur_cnt+1
                elif not visited[nex_x][nex_y]:
                    visited[nex_x][nex_y] = True
                    q.append((nex_x,nex_y,cur_cnt+1))

ans = 0
for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            ans = max(ans, bfs(i,j))

print(ans)