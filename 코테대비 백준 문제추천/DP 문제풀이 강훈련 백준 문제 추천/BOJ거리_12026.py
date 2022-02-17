# import sys

# input = sys.stdin.readline

# n = int(input())
# block = list(input().strip())
# inf = sys.maxsize
# dp = [inf] * (n)

# def returnPre(x):
#     if x == 'B':
#         return 'J'
#     if x == 'O':
#         return 'B'
#     if x == 'J':
#         return 'O'

# dp[0] = 0
# for i in range(1,n):
#     prev = returnPre(block[i])
#     for j in range(i):
#         if block[j] == prev:
#             dp[i] = min(dp[i], dp[j]+pow(i-j, 2))

# print(dp[n-1] if dp[n-1] != inf else -1)

















import sys

input = sys.stdin.readline

n = int(input())
block = list(input().strip())
inf = sys.maxsize
dp = [inf] * (n)

def prev_word(x):
    if x == 'B':
        return 'J'
    if x == 'O':
        return 'B'
    if x == 'J':
        return 'O'

dp[0] = 0
for i in range(1,n):
    prev = prev_word(block[i])
    for j in range(i):
        if block[j] == prev:
            dp[i] = min(dp[i], dp[j]+pow(i-j,2))

print(-1 if dp[n-1] == inf else dp[n-1])