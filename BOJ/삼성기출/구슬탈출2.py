import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
red = []
blue = []
board = []
for i in range(n):
    line = list(input().strip())
    board.append(line)
    if not red or not blue:
        for j in range(m):  
            if line[j] == 'B':
                blue = [i,j]
            elif line[j] == 'R':
                red = [i,j]

def bfs():
    q = collections.deque()
    q.append((red, blue))
    visited = []
    visited.append((red,blue))
    count = 0
    while q:
        for _ in range(len(q)):
            r, b = q.popleft()
            if count > 10:
                print(-1)
                return
            if board[r[0]][r[1]] == 'O':
                print(count)
                return
            for i in [[0,1],[0,-1],[1,0],[-1,0]]:
                nr = [r[0]+i[0], r[1]+i[1]]
                while True:
                    if board[nr[0]][nr[1]] == '#':
                        nr = [nr[0]-i[0], nr[1]-i[1]]
                        break
                    if board[nr[0]][nr[1]] == 'O':
                        break
                    nr = [nr[0]+i[0], nr[1]+i[1]]
                nb = [b[0]+i[0], b[1]+i[1]]
                while True:
                    if board[nb[0]][nb[1]] == '#':
                        nb = [nb[0]-i[0], nb[1]-i[1]]
                        break
                    if board[nb[0]][nb[1]] == 'O':
                        break
                    nb = [nb[0]+i[0], nb[1]+i[1]]
                if board[nb[0]][nb[1]] == 'O':
                    continue
                if nr == nb:
                    if abs(nr[0]-r[0]) + abs(nr[1] - r[1]) > abs(nb[0]-b[0]) + abs(nb[1] - b[1]):
                        nr = [nr[0]-i[0], nr[1]-i[1]]
                    else:
                        nb = [nb[0]-i[0], nb[1]-i[1]]
                if (nr, nb) not in visited:
                    visited.append((nr,nb))
                    q.append((nr,nb))
        count += 1
    print(-1)

bfs()




