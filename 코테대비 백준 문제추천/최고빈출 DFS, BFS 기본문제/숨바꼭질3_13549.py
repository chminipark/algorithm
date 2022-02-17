import sys
import collections
input = sys.stdin.readline

n, k = map(int, input().split())

if n == k:
    print(0)
    sys.exit()

def bfs():
    q = collections.deque()
    q.append((n, 0))
    inf = sys.maxsize
    time_list = [inf] * (100001)
    # idx = n
    # while idx < 100001:
    #     time_list[idx] = 0
    #     idx = idx*2

    while q:
        cur, time = q.popleft()

        plus = cur+1
        minus = cur-1
        jump = cur*2

        if 0 <= plus <= 100000 and time_list[plus] > time+1:
            time_list[plus] = time+1
            q.append((plus, time+1))
        if 0 <= minus <= 100000 and time_list[minus] > time+1:
            time_list[minus] = time+1
            q.append((minus, time+1))
        if 0 <= jump <= 100000 and time_list[jump] > time:
            time_list[jump] = time
            q.append((jump, time))
    
    return time_list[k]

print(bfs())