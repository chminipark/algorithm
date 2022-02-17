# import sys
# import math

# input = sys.stdin.readline

# ans = []
# def solution():
#     k = int(input())
#     k_list = list(map(int, input().split()))
#     dp = [[0] * k for _ in range(k)]

#     for j in range(1, k):
#         for i in range(j-1, -1, -1):
#             min_sum = math.inf
#             for k in range(j-i):
#                 min_sum = min(min_sum, dp[i][i+k] + dp[i+k+1][j])
#             dp[i][j] = min_sum + sum(k_list[i:j+1])

#     ans.append(dp[0][k-1])

# t = int(input())
# for _ in range(t):
#     solution()

# for i in ans:
#     print(i)

# '''
#     A   B   C   D
# A   0
# B
# C
# D

# '''

import sys
import math

input = sys.stdin.readline

ans = []
def solution():
    n = int(input())
    k_list = list(map(int, input().split()))

    dp = [[0]*n for _ in range(n)]

    for j in range(1, n):
        for i in range(j-1, -1, -1):
            min_sum = math.inf
            for k in range(j-i):
                min_sum = min(min_sum, dp[i][i+k] + dp[i+k+1][j])
            dp[i][j] = min_sum + sum(k_list[i:j+1])
    ans.append(dp[0][n-1])

t = int(input())
for _ in range(t):
    solution()

for i in ans:
    print(i)


'''
    A   B   C   D
A   0   AB  AC  
B       0   BC  BD
C           0   CD     
D               0
'''


# import math

# ans = []


# def solve():
#     n = int(input())
#     arr = [int(x) for x in input().split()]
#     rst = [[0 for _ in range(n)] for _ in range(n)]
#     for j in range(1, n):
#         for i in range(j-1, -1, -1):
#             small = math.inf
#             for k in range(j-i):
#                 small = min(small, rst[i][i+k] + rst[i+k+1][j])
#             rst[i][j] = small + sum(arr[i:j+1])
# #   print(rst[0][n-1])
#     ans.append(rst[0][n-1])


# t = int(input())
# for _ in range(t):
#     solve()

# for i in ans:
#     print(i)
