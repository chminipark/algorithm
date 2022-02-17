import sys
input = sys.stdin.readline

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

answer = 0
stack = []
def solution(idx):
    global answer

    if idx >= n:
        # print(stack, idx)
        if idx > n:
            stack.pop()
        answer = max(answer, sum(stack))
        return

    for i in range(idx, n):
        t, p = n_list[i][0], n_list[i][1]
        stack.append(p)
        solution(i+t)
        if stack:
            stack.pop()

solution(0)
print(answer)
