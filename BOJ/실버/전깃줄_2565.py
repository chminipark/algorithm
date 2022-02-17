import sys
input = sys.stdin.readline

cnt = int(input())
line = [list(map(int, input().split())) for _ in range(cnt)]

line.sort(key= lambda x:x[0])

dp = [1 for _ in range(cnt)]
for i in range(cnt):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(cnt-max(dp))