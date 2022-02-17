# import sys

# input = sys.stdin.readline

# weight_count = int(input())
# weight_list = list(map(int, input().split()))
# item_count = int(input())
# item_list = list(map(int, input().split()))

# dp = [[0]*15001]*(weight_count+1)
# memo = [0]*40001

# def scale(left, right, start, end):
#     diff = abs(left - right)

#     if diff <= 40000:
#         memo[diff] = 1

#     if start == end:
#         return

#     if dp[start][diff] == 0:
#         scale(left + weight_list[start], right, start+1, end)
#         scale(left, right + weight_list[start], start+1, end)
#         scale(left, right, start+1, end)
#         dp[start][diff] = 1

# scale(0, 0, 0, weight_count)

# for i in item_list:
#     if memo[i] == 1:
#         print('Y', end=' ')
#     else:
#         print('N', end=' ')

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

weight_count = int(input())
weight_list = list(map(int, input().split()))
item_count = int(input())
item_list = list(map(int, input().split()))

check = [[0]*15001 for _ in range(weight_count)]
# possible = [0]*15001
possible = set()

def scale(start, end, left, right):
    diff = abs(left - right)
    # possible[diff] = 1
    possible.add(diff)

    if start == end:
        return
    
    if check[start][diff] == 0:
        check[start][diff] = 1
        scale(start+1, end, left+weight_list[start], right)
        scale(start+1, end, left, right+weight_list[start])
        scale(start+1, end, left, right)

scale(0, weight_count, 0, 0)

for i in item_list:
    print('Y' if i in possible else 'N', end=' ')

# for i in item_list:
#     if i > 15000:
#         print('N', end=' ')
#     else:
#         print('Y' if possible[i] == 1 else 'N', end= ' ')

