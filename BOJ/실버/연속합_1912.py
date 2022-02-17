import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(1,n):
    dp[i] = max(n_list[i]+dp[i-1], n_list[i])

print(max(dp))