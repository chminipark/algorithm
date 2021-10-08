# import sys
# input = sys.stdin.readline

# n = int(input())
# n_list = list(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))

# n_list.sort()

# def binarySearch(target):
#     global n_list
#     left = 0
#     right = len(n_list)-1
#     while left <= right:
#         mid = (left+right)//2
#         if n_list[mid] == target:
#             return mid
#         elif target < n_list[mid]:
#             right = mid-1
#         else:
#             left = mid+1
#     return -1

# def range_m(index, target):
#     global n_list
#     low, high = -1, -1
#     for i in range(index, len(n_list)):
#         if n_list[i] == target:
#             high += 1
#     for i in range(index, -1, -1):
#         if n_list[i] == target:
#             low += 1
#     return low+high

# answer = []
# for i in m_list:
#     index = binarySearch(i)
#     if index == -1:
#         answer.append('0')
#     else:
#         answer.append(str(range_m(index, i)+1))

# print(' '.join(answer))

## 시간초과...

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def down(target):
    global n_list
    left = 0
    right = len(n_list)-1

    while left <= right:
        mid = (left+right)//2
        if n_list[mid] >= target:
            right = mid-1
        elif n_list[mid] < target:
            left = mid+1
    return left

def up(target):
    global n_list
    left = 0
    right = len(n_list)-1

    while left <= right:
        mid = (left+right)//2
        if n_list[mid] > target:
            right = mid-1
        elif n_list[mid] <= target:
            left = mid+1
    return left

for i in m_list:
    print(up(i)-down(i), end=' ')
