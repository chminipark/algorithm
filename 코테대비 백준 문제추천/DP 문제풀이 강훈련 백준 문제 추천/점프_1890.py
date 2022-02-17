# import sys

# input = sys.stdin.readline

# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0]*(n) for _ in range(n)]
# dp[0][0] = 1

# for i in range(n):
#     for j in range(n):
#         if i == n-1 and j == n-1:
#             break
#         jumpcnt = matrix[i][j]
#         # 오른쪽
#         if j + jumpcnt < n:
#             dp[i][j+jumpcnt] += dp[i][j]
#         # 아래
#         if i + jumpcnt < n:
#             dp[i+jumpcnt][j] += dp[i][j]

# print(dp[n-1][n-1])








import sys

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(n) for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break

        jump_cnt = matrix[i][j]
        down = jump_cnt+i
        right = jump_cnt+j

        if down < n:
            
            dp[down][j] += dp[i][j]
        if right < n:
            dp[i][right] += dp[i][j]

print(dp[-1][-1])