import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
dp1 = [1] * (n)
dp2 = [1] * (n)

for i in range(n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

for i in reversed(range(n)):
    for j in reversed(range(i, n)):
        if n_list[i] > n_list[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

ans = 1
for increase, decrease in zip(dp1, dp2):
    ans = max(ans, (increase+decrease)-1)

print(ans)