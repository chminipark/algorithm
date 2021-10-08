import collections
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

q = collections.deque()
q.append(board)

def zboard():
    return [[0 for _ in range(n)] for _ in range(n)]

while q:
    b = q.popleft()
    for i in ['up', 'down', 'left', 'right']:
        up = zboard()
        if i == 'up':
            for x in range(n):
                a = 0
                for y in range(n):
                    if board[y][x] != 0 and a == 0:
                        a = board[y][x]
                        
