import sys
import itertools

_input = sys.stdin.readline

N = int(_input())
S = []
for _ in range(N):
    S.append(list(map(int, _input().split())))

start = []
minAns = float('Inf')

def dfs():
    global minAns
    if N//2 == len(start):
        start_sum = 0
        link_sum = 0
        for x,y in itertools.combinations(start, 2):
            start_sum += S[x-1][y-1]
            start_sum += S[y-1][x-1]
        link = list(set(range(1,N+1))-set(start))
        for x,y in itertools.combinations(link, 2):
            link_sum += S[x-1][y-1]
            link_sum += S[y-1][x-1]
        diff = abs(start_sum - link_sum)
        if minAns > diff:
            minAns = diff
        return

    for i in range(1,N+1):
        if i in start: continue
        if start and start[-1] > i: continue
        start.append(i)
        dfs()
        start.pop()

dfs()
print(minAns)

