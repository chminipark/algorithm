import sys
import collections

input = sys.stdin.readline

a, b = map(int, input().split())

q = collections.deque()
q.append((a,0))
ans = 1
while q:
    cur, cnt = q.popleft()
    multi = cur*2
    add = cur*10+1

    if multi == b or add == b:
        print(cnt+2)
        sys.exit()
    if multi < b:
        q.append((multi, cnt+1))
    if add < b:
        q.append((add, cnt+1))

print(-1)