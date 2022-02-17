import sys

input = sys.stdin.readline

dp = [0] * (5001)
dp[2] = 1
dp[4] = 2
for i in range(6,5001,2):
    dp[i] = dp[i-2] + (i//2) - 1

t = int(input())
ans = []
for _ in range(t):
    l = int(input())
    ans.append(dp[l]%1000000007)

print(*ans, sep='\n')







'''
1 0
2 1
4 2
6 4 ((())),()()(),(())(),()(()) 1 + 2 + 1
8   ()()()() 1 + 3, 2, 1 = 7
10 1 + 4, 3, 2, 1 = 11

dp[i] = dp[i-2] + (i//2) - 1      + 1 


'''