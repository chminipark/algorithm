# import sys
# input = sys.stdin.readline

# k, n = map(int, input().split())
# k_list = []
# for _ in range(k):
#     k_list.append(int(input()))

# k_list.sort()

# def islan(length):
#     global k_list, n
#     cnt = 0
#     for i in range(len(k_list)-1, -1, -1):
#         if k_list[i]//length == 0:
#             return False
#         cnt += k_list[i]//length
#         if cnt >= n:
#             return True
#     else:
#         return False

# last = k_list[-1]
# while 1:
#     if islan(last):
#         break
#     else:
#         last = last//2

# last = (last*2)-1
# while 1:
#     if islan(last):
#         break
#     else:
#         last -= 1

# print(last)

## 시간초과.. 이분탐색은 for문 돌리면 안될듯..





import sys
input = sys.stdin.readline

k, n = map(int, input().split())
k_list = [int(input()) for _ in range(k)]

low, up = 1, max(k_list)
result = 0

while low <= up:
    mid = (low+up)//2
    cut_sum = sum([(i//mid) for i in k_list])

    if cut_sum >= n:
        result = mid
        low = mid + 1
    elif cut_sum < n:
        up = mid - 1

print(result)