import sys

_input = sys.stdin.readline

N, M = map(int, _input().split())
result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    else:
        for i in range(1, N+1):
            if result and i <= result[-1]:
                continue
            result.append(i)
            dfs()
            result.pop()

dfs()