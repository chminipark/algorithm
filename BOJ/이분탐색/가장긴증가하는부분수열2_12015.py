import bisect
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [a[0]]

for i in range(1, n):
    if dp[-1] < a[i]:
        dp.append(a[i])
    else:
        idx = bisect.bisect_left(dp, a[i])
        dp[idx] = a[i]

print(len(dp))