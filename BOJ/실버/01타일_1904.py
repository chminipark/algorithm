# import sys

# input = sys.stdin.readline

# N = int(input())

# n_2 = 1
# n_1 = 2
# ans = 0

# for i in range(2, N):
#     ans = n_1 + n_2
#     n_2 = n_1
#     n_1 = ans

# print(ans%15746)

# 시간초과...

import sys

input = sys.stdin.readline

N = int(input())

dp = [0]*1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[N]) 