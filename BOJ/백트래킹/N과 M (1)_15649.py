import sys
sys.setrecursionlimit(10**9)

def dfs():
    if len(stack) == m:
        print(*stack)
        return

    for i in range(1, n+1):
        if visited[i]: continue
        visited[i] = True
        stack.append(i)
        dfs()
        stack.pop()
        visited[i] = False

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    stack = []
    visited = [False] * (n+1) 
    dfs()