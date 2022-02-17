def solution(m, n, board):
    answer = 0

    list_board = []
    for i in board:
        list_board.append(list(i))

    def erase():
        to_erase = set()
        for i in range(m-1):
            for j in range(n-1):
                word = list_board[i][j]
                if word == '1':
                    continue
                if list_board[i][j+1] == word and list_board[i+1][j] == word and list_board[i+1][j+1] == word:
                    to_erase.add((i,j))
                    to_erase.add((i+1,j))
                    to_erase.add((i,j+1))
                    to_erase.add((i+1,j+1))
        return to_erase

    def arrange():
        for j in range(n):
            for i in reversed(range(m-1)):
                word = list_board[i][j]
                h = i+1
                ismove = False
                while h < m:
                    if list_board[h][j] == '1':
                        h += 1
                        ismove = True
                    else:
                        break
                if ismove:
                    list_board[i][j] = '1'
                    list_board[h-1][j] = word
    
    to_erase_block = erase()

    while to_erase_block:
        answer += len(to_erase_block)
        for i, j in to_erase_block:
            list_board[i][j] = '1'
        arrange()
        to_erase_block.clear()
        to_erase_block = erase()

    return answer

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

'''
4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	14
6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15
'''

'''
"TTTANT"
"RRFACC"
"RRRFCC"
"TRRRAA"
"TTMMMF"
"TMMTTJ"
'''

# 30*30*8