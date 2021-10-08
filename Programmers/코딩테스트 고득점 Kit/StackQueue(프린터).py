def solution(priorities, location):
    answer = 0
    import collections
    dq = collections.deque((v,i) for i, v in enumerate(priorities))

    while True:
        item = dq.popleft()

        if dq and item[0] < max(dq)[0]:
            dq.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    
    return answer

import collections
priorities = [2, 1, 3, 2]
dq = collections.deque([(v,i) for i, v in enumerate(priorities)])
print(dq)