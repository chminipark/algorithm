# import sys

# input = sys.stdin.readline

# n = int(input())
# dp = [[(0,0)]*(4) for _ in range(n)]
# # (cnt, buffer)
# dp[0][0][0] = 1
# dp[0][0][1] = 0


# for i in range(1,n):
#     for j in range(4):
#         if j == 0:
#             dp[i][j]





















'''
1 : 1       1
2 : 11      2
3 : 111     3
4 : 1111    4
5 : 11111   5
6 : 111234  6
7 : 1112344 9
'''

dp = [i for i in range(101)]
for i in range(7, 101):
    dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
print(dp[int(input())])