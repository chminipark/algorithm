import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

low, up = 0, max(n_list)-1
result = 0

while low <= up:
    mid = (low+up)//2
    cut_sum = sum([(i-mid) for i in n_list if i >= mid])
    if cut_sum >= m:
        result = mid
        low = mid+1
    elif cut_sum < m:
        up = mid-1

print(result)