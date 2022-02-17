import sys
import collections

input = sys.stdin.readline

a = input().strip()
b = input().strip()
dp = [[0] * (len(a)+1) for _ in range(len(b)+1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i-1] == a[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

def findLCS():
    ans = ''
    x = len(b) 
    y = len(a)
    now = dp[-1][-1]
    while now != 0:
        if now-1 == dp[x-1][y] and now-1 == dp[x][y-1]:
            ans = b[x-1] + ans
            x -= 1
            y -= 1
            now -= 1
        elif dp[x-1][y] > dp[x][y-1]:
            x -= 1
        else:
            y -= 1
    
    return ans

print(dp[-1][-1])
print(findLCS())
