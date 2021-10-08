import heapq
import sys
input = sys.stdin.readline

def solution(file: list):
    heapq.heapify(file)

    ans = 0
    while len(file) >= 2:
        summ = 0
        a, b = heapq.heappop(file), heapq.heappop(file)
        summ += a+b
        ans += summ
        heapq.heappush(file, summ)
    
    return ans


answer = []
for _ in range(int(input())):
    k = int(input())
    k_list = list(map(int, input().split()))
    answer.append(solution(k_list))

for i in answer:
    print(i)
