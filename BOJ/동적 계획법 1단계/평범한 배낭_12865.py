# import sys

# input = sys.stdin.readline

# n, k = map(int, input().split())
# item_list = [(-1,-1)]
# for _ in range(n):
#     w, v = map(int, input().split())
#     item_list.append((w,v))

# dp = [[0] * (k+1) for _ in range(n+1)]

# for i in range(1, n+1):
#     for j in range(1, k+1):
#         w = item_list[i][0]
#         v = item_list[i][1]
#         if j < w:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

# print(dp[n][k])


import sys

input = sys.stdin.readline

n, k = map(int, input().split())
item = [(-1,-1)]
for _ in range(n):
    w, v = map(int, input().split())
    item.append((w,v))

dp = [[0]*(k+1)]*(n+1)

for i in range(1, n+1):
    for j in range(1, k+1):
        current_weight = item[i][0]
        current_value = item[i][1]

        if j < current_weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-current_weight]+current_value)

print(dp[-1][-1])

'''
        1   2   3   4   5   6   7
6 13    0   0   0   0   0   13  13
4 8     0   0   0   8   8   13  13
3 6     0   0   6   8   8   13  14
5 12    0   0   6   8   12  13  14

dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

'''