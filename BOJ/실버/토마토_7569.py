import collections
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
box = []
layer = []


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

q = collections.deque()

for z in range(h):
    for y in range(n):
        line = list(map(int, input().split()))
        for x in range(m):
            if line[x] == 1:
                q.append((z,y,x))
        layer.append(line)
    else:
        box.append(layer)
        layer = []


# for z in range(h):
#     for y in range(n):
#         for x in range(m):
#             if box[z][y][x] == 1:
#                 q.append((z,y,x))

while q:
    z, y, x = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                q.append((nz,ny,nx))

ans = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 0:
                print(-1)
                sys.exit(0)
            else:
                ans = max(ans, box[z][y][x])

print(ans-1)