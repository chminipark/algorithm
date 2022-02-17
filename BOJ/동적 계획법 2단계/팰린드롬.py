import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for j in range(1, n):
    for i in range(j-1, -1, -1):
        if n_list[i] != n_list[j]:
            dp[i][j] = 0
            continue
        start, end = i+1, j-1
        if start > end:
            dp[i][j] = 1
            continue
        if dp[start][end] == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = 0

m = int(input())
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    ans.append(dp[a-1][b-1])

for i in ans:
    print(i)

            



'''
  1 2 3 4 5 6 7
1 1 0 1 ? ? 
2   1   ?
3     1   
4       1 
5
6
7
'''