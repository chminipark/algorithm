# #### DFS

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]
inf = sys.maxsize
dp = [[-1] * (1<<n) for _ in range(n)]

def dfs(cur, bit):
    if bit == (1 << n) - 1:
        return 0
    if dp[cur][bit] != -1:
        return dp[cur][bit]
    dp[cur][bit] = inf
    for i in range(n):
        if bit & (1 << i):
            continue
        dp[cur][bit] = min(dp[cur][bit], dfs(cur+1, bit | (1<<i)) + d[cur][i])
    return dp[cur][bit]

print(dfs(0,0))


### for 문

# import sys

# input = sys.stdin.readline

# def bit_counting(x):
#     ans = 0
#     while x:
#         ans += (x & 1)
#         x = (x >> 1)
#     return ans

# n = int(input())
# d = [list(map(int, input().split())) for _ in range(n)]
# inf = sys.maxsize
# dp = [inf] * (1 << n)
# dp[0] = 0

# for i in range(len(dp)):
#     k = bit_counting(i)
#     for j in range(n):
#         if i & (1 << j): continue
#         dp[i | 1 << j] = min(dp[i | 1 << j], dp[i] + graph[k][j])

# print(dp[-1])




not (0b1011 & 0b0100)