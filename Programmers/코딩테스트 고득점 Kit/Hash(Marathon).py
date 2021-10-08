def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("")

    for p, c in zip(participant, completion):
        if p != c:
            answer = p
            break

    return answer


p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]

solution = solution(p, c)
print(solution)