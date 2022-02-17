import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

left, right = 0, n-1
x = sys.maxsize
ans = []

while left < right:
    mixed = abs(n_list[left]+n_list[right])
    if mixed < x:
        x = mixed
        ans = [n_list[left], n_list[right]]
    if n_list[left]+n_list[right] > 0:
        right -= 1
    else:
        left += 1

ans.sort()
print(ans[0], ans[1]) 