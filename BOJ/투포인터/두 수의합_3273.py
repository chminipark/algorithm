import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
x = int(input())

n_list.sort()
left, right = 0, n-1

ans = 0
while left != right:
    if n_list[left]+n_list[right] < x:
        left += 1
    elif n_list[left]+n_list[right] > x:
        right -= 1
    else:
        ans += 1
        left += 1

print(ans)