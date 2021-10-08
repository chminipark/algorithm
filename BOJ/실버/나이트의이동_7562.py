import sys
import collections
input = sys.stdin.readline

can = [(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2)]

def bfs(n, current, to_move):
    matrix = [[0]*n for _ in range(n)]
    q = collections.deque()
    q.append((current[1],current[0]))

    while q:
        x, y = q.popleft()
        
        for i in can:
            nx = x + i[0]
            ny = y + i[1]
            if nx == to_move[1] and ny == to_move[0]:
                return matrix[x][y]+1
            elif 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] + 1
                    q.append((nx, ny))
    
t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    current = list(map(int, input().split()))
    to_move = list(map(int, input().split()))
    if current == to_move:
        answer.append(0)
    else:
        answer.append(bfs(n, current, to_move))

for i in answer:
    print(i)