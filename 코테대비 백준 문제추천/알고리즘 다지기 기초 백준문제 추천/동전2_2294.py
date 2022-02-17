import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
inf = sys.maxsize
dp = [inf] * (k+1)
dp[0] = 0
for c in coin:
    for i in range(c, k+1):
        dp[i] = min(dp[i-c] + 1, dp[i])

print(-1 if dp[-1] == inf else dp[-1])


'''
    0   1   2   3   4   5   6   7   8   9
1   0   1   2   3   4   5   6   7   8   9
2   0   0   1   2   2   3   3   4   4   5
3   0   0   0   1   2   2

    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
1   1   2   3   4   5   6   7   8   9   10
5                   1   2                2                    
12                                              1   2       

'''