# def solution(numbers, target):
#     answer = 0
#     q = [(0,0)]
#     N = len(numbers)

#     while q:
#         current_sum, current_idx = q.pop()

#         if current_idx == N and current_sum == target:
#             answer += 1
#             continue
#         if current_idx == N:
#             continue

#         number = numbers[current_idx]
#         q.append((current_sum+number, current_idx+1))
#         q.append((current_sum-number, current_idx+1))

#     return answer

# n = [1,1,1,1,1]
# t = 3

# print(solution(n,t))



# 완전탐색
from itertools import product
def solution(numbers, taregt):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(taregt)


# bfs
from collections import deque

def solution(numbers, target):
    answer = 0

    q = deque([(0,0)])

    while q:
        current_sum, num_idx = q.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1

        else:
            number = numbers[num_idx]
            q.append((current_sum+number, num_idx + 1))
            q.append((current_sum-number, num_idx + 1))

    return answer


# dfs
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if (idx == N and target == value):
        answer += 1
        return
    if (idx == N):
        return

    DFS(idx+1, numbers, target, vlaue+numbers[idx])
    DFS(idx+1, numbers, target, vlaue-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer