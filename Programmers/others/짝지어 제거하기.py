def solution(s):
    stack = []

    for i in range(len(s)):
        stack.append(s[i])
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    if not stack:
        return 1
    else:
        return 0

print(solution('baabaa'))
