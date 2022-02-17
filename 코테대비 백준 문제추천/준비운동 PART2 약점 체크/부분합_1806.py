import sys

input = sys.stdin.readline

n, s = map(int, input().split())
n_list = list(map(int, input().split()))

p_list = [0]
p_value = 0
for i in n_list:
    p_value += i
    p_list.append(p_value)

left, right = 0, 1
ans = sys.maxsize
while right != n+1:
    summ = p_list[right] - p_list[left]
    if summ < s:
        right += 1
    else:
        ans = min(ans, right - left)
        if left + 1 == right:
            left += 1
            right += 1
        else:
            left += 1

print(0 if ans == sys.maxsize else ans)