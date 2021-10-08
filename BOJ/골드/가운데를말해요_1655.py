import sys
import heapq
input = sys.stdin.readline

n = int(input())
leftheap = []
rightheap = []
result = []

for _ in range(n):
    num = int(input())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-num, num))
    else:
        heapq.heappush(rightheap, (num, num))
    
    if rightheap and leftheap[0][1] > rightheap[0][1]:
        left = heapq.heappop(leftheap)[1]
        right = heapq.heappop(rightheap)[0]

        heapq.heappush(leftheap, (-right,right))
        heapq.heappush(rightheap, (left, left))
    
    result.append(leftheap[0][1])

for i in result:
    print(i)
    
    