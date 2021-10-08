import collections
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
box = []
q = collections.deque()

for i in range(n):
    line = list(map(int, input().split()))
    box.append(line)
    for j in range(m):
        if line[j] == 1:
            q.append((i,j))

# box = [list(map(int, input().split())) for _ in range(n)]
# q = collections.deque()
# for i in range(n):
#     for j in range(m):
#         if box[i][j] == 1:
#             q.append((i,j))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))

# box = sum(box, [])
# if 0 in box:
#     print(-1)
# else:
#     print(max(box)-1)

ans = 0
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans-1)