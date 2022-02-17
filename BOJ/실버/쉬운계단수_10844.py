import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = dp[i-1][1]

    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    
    dp[i][9] = dp[]

