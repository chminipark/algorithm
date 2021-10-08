import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
way_list = list(map(int, input().split()))

print(mapp)
print(move_list)

def toMove(current, D):
    if D == 1:
        return [current[0], current[1]+1]
    elif D == 2:
        return [current[0], current[1]-1]
    elif D == 3:
        return [current[0]-1, current[1]]
    elif D == 4:
        return [current[0]+1, current[1]]

dice_way = [1,3,4,2,5,6]
def dice(to_move):


# for to_move in move_list:
