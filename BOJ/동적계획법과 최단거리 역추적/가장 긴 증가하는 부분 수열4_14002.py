import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
dp = [1] * n
memo = [set() for _ in range(n)]

for i in range(n):
    temp = memo[i]
    for j in range(i):
        if n_list[i] > n_list[j]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
                memo[i] = temp | memo[j] | {n_list[j], n_list[i]}

max_cnt = max(dp)
if max_cnt == 1:
    print(max_cnt)
    print(n_list[0])
    sys.exit()

print(max_cnt)
for i in range(n-1, -1, -1):
    if len(memo[i]) == max_cnt:
        for j in sorted(list(memo[i])):
            print(j, end=' ')
        else:
            sys.exit()
