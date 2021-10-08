import collections
import sys
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

k = int(input())
for _ in range(k):
    w,h = map(int, input().split())
    board[h][w] = 'A'

# k_list = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
l_list = collections.deque()
for _ in range(l):
    l_list.append(list(input().strip()))

snake = collections.deque()
snake.append([0,0])
board[0][0] = 1

way = [0,1]
second = 0
def changeway(d, way):
    if d == 'L':
        if way == [-1,0]:
            return [0,-1]
        elif way == [0,-1]:
            return [1,0]
        elif way == [1,0]:
            return [0,1]
        else:
            return [-1,0]
    elif d == 'D':
        if way == [-1,0]:
            return [0,1]
        elif way == [0,1]:
            return [1,0]
        elif way == [1,0]:
            return [0,-1]
        else:
            return [-1,0]

l_pop = []
second = 0
to_move = []
while True:
    second += 1
    if l_list and not l_pop:
        l_pop = l_list.popleft()
    if int(l_pop[0]) == second:
        way = changeway(l_pop[1], way)
        l_pop.clear()
    to_move.clear()
    to_move.append(snake[0][0]+way[0])
    to_move.append(snake[0][1]+way[1])
    if not (0 <= to_move[0] < n and 0 <= to_move[1] < n):
        break
    elif board[to_move[0]][to_move[1]] == 'A':
        snake.appendleft(to_move)
        board[to_move[0]][to_move[1]] = 1
    else:
        to_remove = snake.pop()
        board[to_remove[0]][to_remove[1]] = 0
        if board[to_move[0]][to_move[1]] == 1:
            break
        else:
            snake.appendleft(to_move)
            board[to_move[0]][to_move[1]] = 1

# def move(to_move, apple):
#     if not apple:
#         snake.appendleft(to_move)
#         board[to_move[0]][to_move[1]] = 1
#         to_remove = snake.pop()
#         board[to_remove[0]][to_remove[1]] = 0
#     else:
#         snake.appendleft(to_move)
#         board[to_move[0]][to_move[1]] = 1

print(second)