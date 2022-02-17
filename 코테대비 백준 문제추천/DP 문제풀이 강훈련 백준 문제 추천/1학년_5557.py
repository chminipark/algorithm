import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
dp = [[0]*(21) for _ in range(n)]
dp[0][n_list[0]] = 1
for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j] != 0:
            plus = j + n_list[i]
            minus = j - n_list[i]
            if plus <= 20:
                dp[i][plus] += dp[i-1][j]
            if minus >= 0:
                dp[i][minus] += dp[i-1][j]

print(dp[n-2][n_list[-1]])








'''
11
8 3 2 4 8 7 2 4 0 8 8


'''