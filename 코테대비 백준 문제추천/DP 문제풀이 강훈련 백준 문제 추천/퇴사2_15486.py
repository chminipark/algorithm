# import sys

# input = sys.stdin.readline

# n = int(input())
# t_list = []
# p_list = []
# for _ in range(n):
#     t, p = map(int, input().split())
#     t_list.append(t)
#     p_list.append(p)

# dp = [0]*(n+1)

# for i in range(n-1,-1,-1):
#     if i + t_list[i] > n:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(dp[i+1], dp[i+t_list[i]] + p_list[i])

# print(dp[0])





import sys

input = sys.stdin.readline

n = int(input())
t_list = []
p_list = []
for _ in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if t_list[i] + i < n+1:
        dp[i] = max(dp[i+1], dp[i+t_list[i]] + p_list[i])

print(dp[0])