import collections
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if n == k:
    print(0)
    print(n)
    sys.exit()

path = [-1] * (100001)
time = 0
def bfs():
    global time
    q = collections.deque()
    q.append((n, 0))

    while q:
        cur_node, cur_time = q.popleft()

        for nex in [cur_node+1, cur_node-1, cur_node*2]:
            if nex == k:
                path[nex] = cur_node
                time = cur_time + 1
                return
            elif 0 <= nex <= 100000 and path[nex] == -1:
                path[nex] = cur_node
                q.append((nex, cur_time+1))

bfs()
cnt = time - 1
idx = k
route = str(k)
while cnt != 0:
    route = str(path[idx]) + ' ' + route
    idx = path[idx]
    cnt -= 1
print(time)
print(str(n) + ' ' + route.strip())