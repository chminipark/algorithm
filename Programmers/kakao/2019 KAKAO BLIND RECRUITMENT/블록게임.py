from collections import defaultdict

def threetwo(cordi, board):
    x, y = cordi
    block = defaultdict(int)

    # 세번째 가로줄
    for i in range(2):
        block[board[x+2][y+i]] += 1
    if len(block) != 1 or list(block.keys())[0] == 0:
        return False
    
    empty, block_num = 0, list(block.keys())[0]
    
    # 첫번재 세로줄
    tmp1, tmp2 = board[x][y], board[x+1][y]
    if tmp1 != tmp2:
        return False
    if not (tmp1 == empty or tmp1 == block_num):
        return False
    block[tmp1] += 2

    # 두번째 세로줄
    tmp1, tmp2 = board[x][y+1], board[x+1][y+1]
    if tmp1 != tmp2:
        return False
    if not (tmp1 == empty or tmp1 == block_num):
        return False
    block[tmp1] += 2

    if len(block) != 2 or block[empty] != 2 or block[block_num] != 4:
        return False
    
    return True



def twothree(cordi, board):
    x, y = cordi
    block = defaultdict(int)
    # 첫번째 줄
    for j in range(3):
        block[board[x][y+j]] += 1
    if len(block) != 2:
        return False
    empty, block_num = sorted(list(block.keys()))
    if empty != 0 or block[empty] != 2:
        return False
    
    # 두번째 줄
    for j in range(3):
        block[board[x+1][y+j]] += 1
    if len(block) != 2:
        return False
    if block[empty] != 2 or block[block_num] != 4:
        return False
    
    return True

def isEmptySpace(cordi, board):
    x, y = cordi
    x -= 1
    while x >= 0:
        if board[x][y] != 0:
            return False
        x -= 1
    return True

def check(cordi, length, board):
    x, y = cordi
    if length == 3:
        if not twothree(cordi, board):
            return False
    if length == 2:
        if not threetwo(cordi, board):
            return False
    for b in range(length):
        if board[x][y+b] == 0:
            if not isEmptySpace((x,y+b), board):
                return False
    return True

def remove(cordi, length, board):
    height = 3 if length == 2 else 2
    x, y = cordi
    for i in range(height):
        for j in range(length):
            board[x+i][y+j] = 0


def solution(board):
    ans = 0
    for i in range(len(board)-2):
        for j in range(len(board)-2):
            if check((i,j), 3, board):
                remove((i,j), 3, board)
                ans += 1
            if check((i,j), 2, board):
                ans += 1
                remove((i,j), 2, board)
        else:
            if check((i,j+1), 2, board):
                ans += 1
                remove((i,j+1), 2, board)
    else:
        for j in range(len(board)-2):
            if check((i+1,j), 3, board):
                ans += 1
                remove((i+1,j), 3, board)
    
    return(ans)


solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])





            
