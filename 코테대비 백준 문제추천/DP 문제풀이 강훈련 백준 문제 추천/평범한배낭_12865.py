import sys

input = sys.stdin.readline

n, k = map(int, input().split())
w_list = [-1]
v_list = [-1]
for _ in range(n):
    weight, value = map(int, input().split())
    w_list.append(weight)
    v_list.append(value)

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1, k+1):
        if w_list[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_list[i]]+v_list[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])




'''
    1   2   3   4   5   6   7   K
    0   0   0   0   0   13  13
    0   0   0   8   8   13  13
    0   0   6   8   8   13  14


dp[i][j] = max(dp[i-1][j], dp[i][j-wei]+value)



'''