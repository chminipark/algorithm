from curses import nonl
import sys

def solution(program):
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    # 방향 1,2,3,4
    cur = [[0,0], 1]

    # FBLR
    def moveAndCheck(w):
        nonlocal min_x, max_x, min_y, max_y
        nonlocal cur
        cnt = 1 if w == 'F' else -1
        if cur[1] == 1:
            nex_cor = [cur[0][0] + cnt, cur[0][1]]
            cur = [nex_cor, cur[1]]
        elif cur[1] == 2:
            nex_cor = [cur[0][0], cur[0][1] + cnt]
            cur = [nex_cor, cur[1]]
        elif cur[1] == 3:
            nex_cor = [cur[0][0] - cnt, cur[0][1]]
            cur = [nex_cor, cur[1]]
        elif cur[1] == 4:
            nex_cor = [cur[0][0], cur[0][1] - cnt]
            cur = [nex_cor, cur[1]]
        
        cur_y, cur_x = cur[0]
        min_y = min(cur_y, min_y)
        max_y = max(cur_y, max_y)
        min_x = min(cur_x, min_x)
        max_x = max(cur_x, max_x)

    def direction(w):
        nonlocal cur
        cnt = 1 if w == 'R' else -1
        nex_dir = cur[1] + cnt
        if nex_dir == 5:
            nex_dir = 1
        if nex_dir == 0:
            nex_dir = 4
        cur = [cur[0], nex_dir]
    
    for i in program:
        if i == 'F' or i == 'B':
            moveAndCheck(i)
        else:
            direction(i)

    return abs(max_x - min_x) * abs(max_y - min_y)

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input())
    answer = []
    for _ in range(t):
        s = input().rstrip()
        answer.append(solution(s))
    print(*answer, sep='\n')
