def solution(priorities, location):
    from collections import deque
    dq = deque([(v, i) for i, v in enumerate(priorities)])
    answer = 0

    while len(dq):
        item = dq.popleft()
        if dq and max(dq)[0] > item[0]:
            dq.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    
    return answer

p = [2, 1, 3, 2]
l = 2
print(solution(p, l))

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.