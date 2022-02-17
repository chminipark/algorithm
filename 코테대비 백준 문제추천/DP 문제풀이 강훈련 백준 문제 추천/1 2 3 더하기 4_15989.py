# dp = [1] * (10001)
# for i in range(2, 10001):
#     dp[i] += dp[i-2]
# for i in range(3, 10001):
#     dp[i] += dp[i-3]

# import sys

# input = sys.stdin.readline
# t = int(input())
# ans = []
# for _ in range(t):
#     n = int(input())
#     ans.append(dp[n])

# print(*ans, sep='\n')














import sys

input = sys.stdin.readline

dp = [1] * (10001)
for i in range(2, 10001):
    dp[i] += dp[i-2]
for i in range(3, 10001):
    dp[i] += dp[i-3]

print(dp[10])
