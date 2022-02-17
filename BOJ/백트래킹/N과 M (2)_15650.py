import sys
sys.setrecursionlimit(10**9)

def dfs():
    if len(stack) == m:
        print(*stack)
        return

    for i in range(1, n+1):
        if stack and stack[-1] >= i:
            continue
        stack.append(i)
        dfs()
        stack.pop()

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    stack = []
    dfs()