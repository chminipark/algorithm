import itertools
import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lab = []
virus = []
wall_list = []
for i in range(n):
    line = list(input().strip().split())
    lab.append(line)
    for j in range(m):
        if line[j] == '2':
            virus.append((i,j))
        elif line[j] == '0':
            wall_list.append((i,j))

answer = float('-inf')
def safeAreaCount(wall):
    global answer
    q = collections.deque()
    for i in virus:
        q.append(i)
    nlab = [i[:] for i in lab]
    for i in wall:
        nlab[i[0]][i[1]] = '1'
    while q:
        v = q.popleft()
        for i in [(1,0), (-1,0), (0,1), (0,-1)]:
            nv = (v[0]+i[0], v[1]+i[1])
            if 0 <= nv[0] < n and 0 <= nv[1] < m:
                if nlab[nv[0]][nv[1]] == '0':
                    q.append(nv)
                    nlab[nv[0]][nv[1]] = '2'

    answer = max(answer ,sum(nlab, []).count('0'))

for i in itertools.combinations(wall_list, 3):
    safeAreaCount(i)

print(answer)
