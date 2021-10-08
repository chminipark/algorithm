def solution(prices):
    from collections import deque
    answer = []
    dq = deque(prices)
    
    while len(dq):
        item = dq.popleft()
        count = 0
        if dq:
            for i in range(len(dq)):
                if item > dq[i]:
                    if i == 0:
                        count = 1
                    break
                count += 1
        answer.append(count)
    
    return answer

p = [1, 2, 3, 2, 3]
sol = solution(p)
print(sol)