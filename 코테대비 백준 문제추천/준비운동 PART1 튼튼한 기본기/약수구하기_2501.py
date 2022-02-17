import sys

input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0
ans = 0
for i in range(1, n+1):
    if n % i == 0:
        ans = i
        cnt += 1
    if cnt == k:
        break

if cnt == k:
    print(ans)
else:
    print(0)