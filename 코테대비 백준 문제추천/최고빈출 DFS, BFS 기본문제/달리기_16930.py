import collections
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
gym = [list(input().strip()) for _ in range(n)]
x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())


def bfs():
    q = collections.deque()
    q.append((x1, y1, 0))
    # (cur_x, cur_y, cur_cnt)
    inf = sys.maxsize
    visited = [[inf] * (m) for _ in range(n)]
    visited[x1][y1] = 0

    while q:
        cur_x, cur_y, cur_cnt = q.popleft()
        for direction in ['up', 'right', 'down', 'left']:
            if direction == 'up':
                k_idx = 1
                nex_x = cur_x - k_idx
                while 0 <= nex_x and k_idx <= k:
                    if nex_x == x2 and cur_y == y2:
                        return cur_cnt+1
                    if gym[nex_x][cur_y] == '#':
                        break
                    if visited[nex_x][cur_y] > cur_cnt+1:
                        visited[nex_x][cur_y] = cur_cnt+1
                        q.append((nex_x, cur_y, cur_cnt+1))
                        k_idx += 1
                        nex_x = cur_x - k_idx
                    else:
                        k_idx += 1
                        nex_x = cur_x - k_idx
            elif direction == 'right':
                k_idx = 1
                nex_y = cur_y + k_idx
                while nex_y < m and k_idx <= k:
                    if cur_x == x2 and nex_y == y2:
                        return cur_cnt+1
                    if gym[cur_x][nex_y] == '#':
                        break
                    if visited[cur_x][nex_y] > cur_cnt+1:
                        visited[cur_x][nex_y] = cur_cnt+1
                        q.append((cur_x, nex_y, cur_cnt+1))
                        k_idx += 1
                        nex_y = cur_y + k_idx
                    else:
                        k_idx += 1
                        nex_y = cur_y + k_idx
            elif direction == 'down':
                k_idx = 1
                nex_x = cur_x + k_idx
                while nex_x < n and k_idx <= k:
                    if nex_x == x2 and cur_y == y2:
                        return cur_cnt+1
                    if gym[nex_x][cur_y] == '#':
                        break
                    if visited[nex_x][cur_y] > cur_cnt+1:
                        visited[nex_x][cur_y] = cur_cnt+1
                        q.append((nex_x, cur_y, cur_cnt+1))
                        k_idx += 1
                        nex_x = cur_x + k_idx
                    else:
                        k_idx += 1
                        nex_x = cur_x + k_idx
            elif direction == 'left':
                k_idx = 1
                nex_y = cur_y - k_idx
                while 0 <= nex_y and k_idx <= k:
                    if cur_x == x2 and nex_y == y2:
                        return cur_cnt+1
                    if gym[cur_x][nex_y] == '#':
                        break
                    if visited[cur_x][nex_y] > cur_cnt+1:
                        visited[cur_x][nex_y] = cur_cnt+1
                        q.append((cur_x, nex_y, cur_cnt+1))
                        k_idx += 1
                        nex_y = cur_y - k_idx
                    else:
                        k_idx += 1
                        nex_y = cur_y - k_idx

    return -1

print(bfs())



# import collections
# import sys

# input = sys.stdin.readline

# n, m, k = map(int, input().split())
# gym = [list(input().strip()) for _ in range(n)]
# x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
