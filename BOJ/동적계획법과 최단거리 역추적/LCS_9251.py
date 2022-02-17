'''
    0   A   C   A   Y   K   P
0   0   0   0   0   0   0
C   0   1   1   1   1   1
A   0   0   1   1   1   1
P   0        
C   0
A   0
K   0
x == y:
dp[i][j] = dp[i-1][j-1]+1
x != y:
dp[i][j] = max(dp[i-1][j], dp[i][j-1])
'''

import sys

input = sys.stdin.readline

A = input().strip()
B = input().strip()

dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
