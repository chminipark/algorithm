# import sys
# import math

# input = sys.stdin.readline

# n = int(input())
# dp = [[''] * n for _ in range(n)]
# for i in range(n):
#     x, y = input().split()
#     dp[i][i] = x+'*'+y

# 532 26
# 53 326

# 532 234
# 345 567



# def multi_matrix(a, b):


# for j in range(1,n):
#     for i in range(j-1,-1,-1):
#         min_sum = math.inf
#         for k in range(j-i):
#             min_sum = min(min_sum)
            

#     a   b   c       d
# a   a   ab  ab c    ab cd
#             a bc
# b       b   bc
# c           c
# d                   d
# '''
# dp[i][j] = dp[i][i+k] * dp[i+k+1][j]

# a = '*'.join(['2','3','4'])
# eval(a)


import sys
import math

input = sys.stdin.readline

n = int(input())
matrix = []
for i in range(n):
    x, y = map(int, input().split())
    matrix.append((x,y))

dp = [[0]*n for _ in range(n)]
for j in range(1,n):
    for i in range(j-1,-1,-1):
        min_sum = math.inf
        for k in range(j-i):
            min_sum = min(min_sum, dp[i][i+k] + dp[i+k+1][j] + (matrix[i][0] * matrix[i+k][1] * matrix[j][1]))
        dp[i][j] = min_sum

print(dp[0][n-1])