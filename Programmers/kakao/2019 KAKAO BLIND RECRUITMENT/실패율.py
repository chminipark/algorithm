from collections import Counter
def solution(N, stages):
    stages_counter = Counter(stages)
    # [failure, stagenum]
    failure = []
    right_cnt = 0
    for i in range(1, N+1):
        left = stages_counter[i]
        right = len(stages) - right_cnt
        if right == 0:
            failure.append([0, i])
            continue
        failure.append([left/right, i])
        right_cnt += left
    
    failure.sort(key=lambda x:(-x[0], x[1]))
    return [i[1] for i in failure]

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(5, [2,2,2,2,2])


'''
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수


'''