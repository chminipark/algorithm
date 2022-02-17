import sys

input = sys.stdin.readline

n = int(input())

dp = [[0,1,1,1,1,1,1,1,1,1]]

for i in range(n-1):
    temp = [0]*10
    for j in range(10):
        if 0 < j < 9:
            temp[j] = dp[i][j-1] + dp[i][j+1]
        elif j == 0:
            temp[j] = dp[i][j+1]
        else:
            temp[j] = dp[i][j-1]
    dp.append(temp)

print(sum(dp[-1])%1000000000)