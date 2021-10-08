import sys
input = sys.stdin.readline

n, c = map(int, input().split())
n_list = [int(input()) for _ in range(n)]

n_list.sort()
low, up = 1, n_list[-1]-n_list[0]
result = 0

def count_router(distance):
    global n_list, n
    current = n_list[0]
    count = 1
    for i in range(1, n):
        if current+distance <= n_list[i]:
            current = n_list[i]
            count += 1
    return count

while low <= up:
    mid = (low+up)//2

    count = count_router(mid)

    if count >= c:
        result = mid
        low = mid+1
    elif count < c:
        up = mid-1

print(result)