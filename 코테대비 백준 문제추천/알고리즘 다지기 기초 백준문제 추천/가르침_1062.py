import sys

input = sys.stdin.readline

n, k = map(int, input().split())
w_list = [set(input().strip()[4:-4]) for _ in range(n)]
alpha = set('antic')
possible = k-5

if possible < 0:
    print(0)
    sys.exit()

ans = 0
for word in w_list:
    unknown = alpha - word
    if not unknown:
        ans += 1
        continue
    else:
        for i in unknown:
            