def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        second = heapq.heappop(scoville)
        mix = first + (second * 2)
        heapq.heappush(scoville, mix)
        answer += 1
    
    if scoville[0] >= K:
        return answer
    else:
        return -1


s = [1, 2, 3, 9, 10, 12]
k = 7

print(solution(s, k))
