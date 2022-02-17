# import sys
# import math

# input = sys.stdin.readline

# def isprime(num):
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     else:
#         return True

# def solution():
#     n = int(input())

#     prime_list = []
#     for i in range(2, n+1):
#         if isprime(i):
#             prime_list.append(i)
    
#     prefix_value = 0
#     prefix_list = [0]
#     for i in prime_list:
#         prefix_value += i
#         prefix_list.append(prefix_value)

#     left, right = 1, 1

#     ans = 0
#     while right < len(prefix_list):
#         summ = prefix_list[right] - prefix_list[left-1]
#         if summ > n:
#             if left == right:
#                 left += 1
#                 right += 1
#             else:
#                 left += 1
#         elif summ < n:
#             right += 1
#         else:
#             ans += 1
#             if left == right:
#                 left += 1
#                 right += 1
#             else:
#                 left += 1
    
#     print(ans)

# solution()

## 시간초과... prefix때문인가.. 검색해보니 에라토스테네스 체로 소수 배열 만들어야 함


import sys

input = sys.stdin.readline

n = int(input())
isprime = [False, False] + [True] * (n-1)
prefix_value = 0
prefix_list = [0]
for i in range(2, n+1):
    if isprime[i]:
        prefix_value += i
        prefix_list.append(prefix_value)
        for j in range(i*2, n+1, i):
            isprime[j] = False

left, right = 1, 1
ans = 0
while right < len(prefix_list):
    summ = prefix_list[right] - prefix_list[left-1]
    if summ > n:
        if left == right:
            left += 1
            right += 1
        else:
            left += 1
    elif summ < n:
        right += 1
    else:
        ans += 1
        left += 1
        right += 1

print(ans)