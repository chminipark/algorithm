import sys

input = sys.stdin.readline

n = int(input())
n_list = [-1] + list(map(int, input().split()))
s = int(input())

pre_list = [0]
pre_value = 0
for i in range(1,n+1):
    pre_value += n_list[i]
    pre_list.append(pre_value)

dp = [[0]*(n+1) for _ in range(4)]
for i in range(1,4):
    for j in range(i*s,n+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-s] + (pre_list[j]-pre_list[j-s]))

print(dp[-1][-1])









'''




7
    35  40  50  10  30  45  60
1       70  90
2       70  90  
3




'''