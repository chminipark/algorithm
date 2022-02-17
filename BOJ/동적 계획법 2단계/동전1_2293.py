# import sys

# input = sys.stdin.readline

# n, k = map(int, input().split())
# coin = []
# for _ in range(n):
#     coin.append(int(input()))

# dp = [[0 for _ in range(k+1)] for _ in range(n)]

# for i in range(1, k+1):
#     if i % coin[0] == 0:
#         dp[0][i] = 1

# for i in range(1, n):
#     if coin[i] <= k:
#         dp[i][coin[i]] = 1
#     for j in range(coin[i]+1, k+1):
#         dp[i][j] = sum([dp[a][j-coin[i]] for a in range(i+1)])

# print(sum([i[-1] for i in dp]))

# '''
#     1   2   3   4   5   6
# 1   1   1   1   1   1   1
# 2   0   1   1   2   2   3
# 5   0   0   0   0   1   1

# '''

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1

for i in coin:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])








'''

    1   2   3   4   5   6
1   1   1   1   1   1   1
2       1   1   2   
5

'''