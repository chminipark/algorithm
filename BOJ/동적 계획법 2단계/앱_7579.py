import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
summ = sum(c_list)

dp = [[0 for _ in range(summ+1)] for _ in range(n+1)]
ans = summ
for i in range(1, n+1):
    size = a_list[i-1]
    cost = c_list[i-1]
    for j in range(1, summ+1):
        if cost < j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], size+dp[i-1][j-cost])
        if dp[i][j] >= m:
            ans = min(j, ans)

print(ans)


'''

5 60
30 10 20 35 40
3 0 3 5 4

dp[i][j] = i번째 앱까지, j=cost만큼 최대 
if j > cost:
    dp[i][j] = dp[i-1][j]
else:
    dp[i][j] = max(dp[i-1][j], value + d[i-1][j-cost])
answer = min(j, answer)
    0   1   2   3   4   5   6   7
0   0   0   0   0   0   0   0   0
30  3   0   0   30  30  30  30  30   
10  0   10  10  40  40  40  40  40
20  3   10  10  40  40  40  60  60
35  5
40  4

'''