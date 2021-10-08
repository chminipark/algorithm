def solution(bridge_length, weight, truck_weights):
    answer = 0
    from collections import deque
    waiting = deque(truck_weights)
    onbridge = deque([0 for i in range(bridge_length)])

    while len(waiting):
         # 트럭 옮기기
        if onbridge[0] != 0:
            onbridge[0] = 0
        onbridge.rotate(-1)

        # 트럭 다리에 올리기
        truck = waiting[0]
        if sum(onbridge) + truck <= weight and onbridge[-1] == 0:
            onbridge[-1] = truck
            waiting.popleft()
        
        answer += 1

    return answer + bridge_length


length = 2
weight = 10
truck = [7,4,5,6]

sol = solution(length, weight, truck)
print(sol)

# from collections import deque
# # onbridge = deque([1 for i in range(3)])
# onbridge = deque([1, 2, 3])
# print(sum(onbridge))
# onbridge[-1]