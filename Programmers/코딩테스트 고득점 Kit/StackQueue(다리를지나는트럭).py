def solution(bridge_length, weight, truck_weights):
    from collections import deque
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque([0]*bridge_length)

    while bridge:
        answer += 1
        bridge.popleft()

        if trucks:
            if sum(bridge) + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
            else:
                bridge.append(0)

    return answer


truck_weights = [7,4,5,6]
weight = 10
bridge_length = 2

solution(bridge_length, weight, truck_weights)



# deque 사용법 노션에 정리 rotate.. extend