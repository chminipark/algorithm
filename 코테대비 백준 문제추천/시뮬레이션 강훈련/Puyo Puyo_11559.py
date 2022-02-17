import sys

def solution(board):

    def checkAndPop(cordi):
        nonlocal board
        color = board[cordi[0]][cordi[1]]
        to_pop = []
        dfs_stack = [cordi]
        dfs_visited = [[False] * (6) for _ in range(12)]
        flag = False

        while dfs_stack:
            cur = dfs_stack.pop()
            to_pop.append(cur)
            dfs_visited[cur[0]][cur[1]] = True

            for x, y in [(1,0), (0,1), (-1,0), (0,-1)]:
                nex_x = cur[0] + x
                nex_y = cur[1] + y

                if 0 <= nex_x < 12 and 0 <= nex_y < 6:
                    if board[nex_x][nex_y] == color and not dfs_visited[nex_x][nex_y]:
                        dfs_stack.append((nex_x, nex_y))
        
        if len(to_pop) >= 4:
            for x, y in to_pop:
                board[x][y] = '.'
            flag = True
        
        return flag
    
    def arrangeLine():
        nonlocal board
        for verti in range(6):
            to_hor = -1
            for i in range(11,-1,-1):
                if board[i][verti] == '.':
                    to_hor = i
                    break
            if to_hor == -1:
                return
            for hor in range(to_hor-1,-1,-1):
                if board[hor][verti] != '.' and hor < to_hor:
                    board[to_hor][verti] = board[hor][verti]
                    board[hor][verti] = '.'

                    for i in range(to_hor-1, -1, -1):
                        if board[i][verti] == '.':
                            to_hor = i
                            break
                    else:
                        return
     
    chaincnt = 0
    isCount = True
    while isCount:
        isCount = False
        for i in range(12):
            for j in range(6):
                if board[i][j] != '.':
                    if checkAndPop((i,j)):
                        isCount = True
        if isCount:
            arrangeLine()
            chaincnt += 1

    print(chaincnt)

if __name__ == '__main__':
    input = sys.stdin.readline
    board = [list(input().rstrip()) for _ in range(12)]
    solution(board)
