# import itertools

# def rgb(rgb_list: list):
#     sum_rgb = 0
#     for j in range(0, N-(N%3), 3):
#         min_sum = float('inf')
#         for i in itertools.permutations([0,1,2], 3):
#             if min_sum > rgb_list[j][i[0]] + rgb_list[j+1][i[1]] + rgb_list[j+2][i[2]]:
#                 min_sum = rgb_list[j][i[0]] + rgb_list[j+1][i[1]] + rgb_list[j+2][i[2]]
#         sum_rgb += int(min_sum)
#     if N%3 != 0:
#         if N%3 == 1:
#             sum_rgb += min(rgb_list[-1])
#         elif N%3 == 2:
#             min_sum = float('inf')
#             for i in itertools.permutations([0,1,2], 2):
#                 if min_sum > rgb_list[-2][i[0]] + rgb_list[-1][i[1]]:
#                     min_sum = rgb_list[-2][i[0]] + rgb_list[-1][i[1]]
#             sum_rgb += int(min_sum)        
#     return sum_rgb

# import sys

# input = sys.stdin.readline

# N = int(input())
# rgb_list = []

# for _ in range(N):
#     rgb_list.append(list(map(int, input().split())))

# print(rgb(rgb_list))

# import sys
# input = sys.stdin.readline

# n = int(input())
# RGB = []
# for i in range(n):
#     RGB.append(list(map(int, input().strip().split())))

# for i in range(1, n):
#     #빨간집
#     RGB[i][0] = min(RGB[i - 1][1], RGB[i - 1][2]) + RGB[i][0]
#     #초록집
#     RGB[i][1] = min(RGB[i - 1][0], RGB[i - 1][2]) + RGB[i][1]
#     #파란집
#     RGB[i][2] = min(RGB[i - 1][0], RGB[i - 1][1]) + RGB[i][2]
# print(min(RGB[n - 1]))


import sys

input = sys.stdin.readline

N = int(input())
n_list = []

for _ in range(N):
    n_list.append(list(map(int, input().split())))

for i in range(1, N):
    n_list[i][0] = min(n_list[i-1][1], n_list[i-1][2]) + n_list[i][0]
    n_list[i][1] = min(n_list[i-1][0], n_list[i-1][2]) + n_list[i][1]
    n_list[i][2] = min(n_list[i-1][0], n_list[i-1][1]) + n_list[i][2]

print(min(n_list[-1]))