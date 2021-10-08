import collections
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
q = collections.deque()
max_time = 100000
time = [0] * (max_time+1)

q.append(n)
while q:
    x = q.popleft()
    if x == k:
        print(time[x])
        break
    for i in [x+1, x-1, x*2]:
        if 0 <= i <= max_time and not time[i]:
            time[i] = time[x] + 1
            q.append(i)
