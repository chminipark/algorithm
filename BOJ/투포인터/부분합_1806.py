import sys
import math

input = sys.stdin.readline

n, s = map(int, input().split())
n_list = list(map(int, input().split()))

prefix_value = 0
prefix_sum = [0]
for i in n_list:
    prefix_value += i
    prefix_sum.append(prefix_value)

left, right = 1, 1

ans = math.inf
while right <= n:
    summ = prefix_sum[right] - prefix_sum[left-1]
    if summ >= s:
        ans = min(ans, right-left+1)
        if left == right:
            left += 1
            right += 1
        else:
            left += 1
    else:
        right += 1

print(0 if ans == math.inf else ans)