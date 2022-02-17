# import sys

# input = sys.stdin.readline

# n, s, m = map(int, input().split())
# n_list = [-1] + list(map(int, input().split()))
# dp = [[False]*(m+1) for _ in range(n+1)]
# dp[0][s] = True

# for i in range(1, n+1):
#     flag = False
#     for j in range(m+1):
#         if dp[i-1][j] == True:
#             down = j - n_list[i]
#             up = j + n_list[i]
#             if 0 <= down:
#                 dp[i][down] = True
#                 flag = True
#             if up <= m:
#                 dp[i][up] = True
#                 flag = True
#     if not flag:
#         print(-1)
#         sys.exit()

# ans = 0
# for i in range(m+1):
#     if dp[n][i]:
#         ans = max(i, ans)
# print(ans)

# '''
# 3 5 10
# 5 3 7

#     0   1   2   3   4   5   6   7   8   9   10
# 5   1                                       1
# 3               1               1
# 7                   1        





# '''



import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())
volume = [-1] + list(map(int, input().split()))
dp = [[False] * (m+1) for _ in range(n+1)]
dp[0][s] = True
for i in range(1, n+1):
    flag = True
    for j in range(m+1):
        if dp[i-1][j]:
            flag = False
            min_v = j-volume[i]
            max_v = j+volume[i]
            if 0 <= min_v:
                dp[i][min_v] = True
            if max_v <= m:
                dp[i][max_v] = True
    if flag:
        print(-1)
        sys.exit()

ans = 0
for i in range(m+1):
    if dp[n][i]:
        ans = max(i, ans)

print(ans)
