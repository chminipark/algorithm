from collections import deque

def solution(board):

    memo = [[float('inf')]*(len(board)) for _ in range(len(board))]
    memo[0][0] = 0
    # [[cordi], direction, dist]
    q = deque()

    if board[1][0] == 0:
        memo[1][0] = 100
        q.append([[1,0], 2, 100])
    if board[0][1] == 0:
        memo[0][1] = 100
        q.append([[0,1], 1, 100])

    direction = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}
    while q:
        cur_cordi, cur_dir, cur_dist = q.popleft()
        cur_x, cur_y = cur_cordi

        for i in range(4):
            nex_x = direction[i][0] + cur_x
            nex_y = direction[i][1] + cur_y

            if 0 <= nex_x < len(board) and 0 <= nex_y < len(board):
                if board[nex_x][nex_y] == 0:
                    nex_dist = cur_dist + 100
                    if cur_dir != i:
                        nex_dist += 500
                    if memo[nex_x][nex_y]+500 > nex_dist:
                        if memo[nex_x][nex_y] > nex_dist:
                            memo[nex_x][nex_y] = nex_dist
                        q.append([[nex_x, nex_y], i, nex_dist])

    return memo[-1][-1]

solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]])
solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]])
