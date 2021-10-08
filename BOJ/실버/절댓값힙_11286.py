import sys
import heapq
input = sys.stdin.readline

n = int(input())
x_list = [int(input()) for _ in range(n)]

heap_abs = []
result = []

for i in x_list:
    if i == 0:
        if heap_abs:
            result.append(heapq.heappop(heap_abs)[1])
        else:
            result.append(0)
    else:
        heapq.heappush(heap_abs, (abs(i), i))

for i in result:
    print(i)
    