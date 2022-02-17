import sys
import collections

input = sys.stdin.readline
# position = 'V', 'H', 'D'

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

if matrix[n-1][n-1] == 1:
    print(0)
    sys.exit()
    
q = collections.deque()
q.append([(0,1),'H'])

def move_right(cur_pos, cur_dir):
    next_pos = (cur_pos[0], cur_pos[1]+1)
    if 0 <= next_pos[0] < n and 0 <= next_pos[1] < n:
        if matrix[next_pos[0]][next_pos[1]] == 0:
            return [(next_pos[0], next_pos[1]), 'H']
    return []

def move_down(cur_pos, cur_dir):
    next_pos = (cur_pos[0]+1, cur_pos[1])
    if 0 <= next_pos[0] < n and 0 <= next_pos[1] < n:
        if matrix[next_pos[0]][next_pos[1]] == 0:
            return [(next_pos[0], next_pos[1]), 'V']
    return []

def move_diago(cur_pos, cur_dir):
    next_pos = (cur_pos[0]+1, cur_pos[1]+1)
    if 0 <= next_pos[0] < n and 0 <= next_pos[1] < n:
        if matrix[next_pos[0]][next_pos[1]] == 0 and matrix[cur_pos[0]+1][cur_pos[1]] == 0 and matrix[cur_pos[0]][cur_pos[1]+1] == 0:
            return [(next_pos[0], next_pos[1]), 'D']
    return []

def check(cur_pos, cur_dir):
    result = []
    if cur_dir == 'H':
        result.append(move_right(cur_pos, cur_dir))
        result.append(move_diago(cur_pos, cur_dir))
    elif cur_dir == 'V':
        result.append(move_down(cur_pos, cur_dir))
        result.append(move_diago(cur_pos, cur_dir))
    else:
        result.append(move_right(cur_pos, cur_dir))
        result.append(move_down(cur_pos, cur_dir))
        result.append(move_diago(cur_pos, cur_dir))
    return result

ans = 0
while q:
    posi, dire = q.popleft()

    for to_add in check(posi, dire):
        if to_add:
            if to_add[0] == (n-1, n-1):
                ans += 1
                continue    
            q.append(to_add)

print(ans)

