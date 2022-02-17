def solution(board, moves):
    stack = []
    ans = 0

    def grab(num):
        for i in range(len(board)):
            if board[i][num] != 0:
                stack.append(board[i][num])
                board[i][num] = 0
                return
    
    def stack_pop():
        nonlocal ans
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            ans += 2
    
    for num in moves:
        grab(num-1)
        stack_pop()

    return ans


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])