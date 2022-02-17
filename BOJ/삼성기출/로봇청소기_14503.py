import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
start, d = (a[0], a[1]), a[2]
room = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def toMove(d):
    if d == 0:
        return (start[0]-1, start[1])
    elif d == 1:
        return (start[0], start[1]+1)
    elif d == 2:
        return (start[0]+1, start[1])
    else:
        return (start[0], start[1]-1)
    
def back(d):
    if d == 0:
        return (start[0]+1, start[1])
    elif d == 1:
        return (start[0], start[1]-1)
    elif d == 2:
        return (start[0]-1, start[1])
    elif d == 3:
        return (start[0], start[1]+1)

turn_off = False
c_if = False
while True:
    if turn_off:
        break
    # 1
    if room[start[0]][start[1]] == 0 and not c_if:
        room[start[0]][start[1]] = 2
        ans += 1

    c_if = False
    # 2
    for _ in range(3):
        nd = d - 1
        if nd == -1:
            nd = 3
        to_move = toMove(nd)
        #
        if room[to_move[0]][to_move[1]] == 0:
            start = to_move
            d = nd
            break
    else:
        to_move = back(d)
        if room[to_move[0]][to_move[1]] != 1:
            start = to_move
            c_if = True
            continue
        else:
            turn_off = True

print(ans)