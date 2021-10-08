import sys
import heapq
input = sys.stdin.readline

n = int(input())
x_list = [int(input()) for _ in range(n)]

heap = []
result = []

for i in x_list:
    if i == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, i)

for i in result:
    print(i)