import sys

input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    sys.exit()
elif n == 1:
    print(1)
    sys.exit()
else:
    memo = [0 for _ in range(n+1)]
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    print(memo[-1])
