import bisect
import collections
import sys

input = sys.stdin.readline

n = int(input())
n_list = [0] + list(map(int, input().split()))
memo = [-sys.maxsize]
idx_list = [0] * (n+1)

for i in range(1, n+1):
    if n_list[i] > memo[-1]:
        memo.append(n_list[i])
        idx_list[i] = len(memo)-1
    else:
        idx_list[i] = bisect.bisect_left(memo, n_list[i])
        memo[idx_list[i]] = n_list[i]

print(len(memo)-1)
idx = len(memo)-1
lis = collections.deque()
for i in range(n, 0, -1):
    if idx_list[i] == idx:
        lis.appendleft(n_list[i])
        idx -= 1
        if idx == 0:
            break
print(*lis)
    