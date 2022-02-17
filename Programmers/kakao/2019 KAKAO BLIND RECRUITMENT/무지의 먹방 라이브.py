# heapq

import heapq

def solution(food_times, k):
    hq = []
    for i in range(len(food_times)):
        # [time, idx]
        heapq.heappush(hq, [food_times[i], i+1])
    
    ans = -1
    pre = 0
    food_cnt = len(food_times)
    while hq:
        t = (hq[0][0] - pre) * food_cnt
        if t <= k:
            pre, _ = heapq.heappop(hq)
            k -= t
            food_cnt -= 1
        else:
            idx = k % food_cnt
            hq.sort(key=lambda x: x[1])
            ans = hq[idx][1]
            break
    
    return ans

# 이분탐색으로도 풀어보기..