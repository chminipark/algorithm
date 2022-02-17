bracket = list(input().strip())

stack = []

def matching(a, b):
    if a == '(' and b == ')':
        return True
    elif a == '[' and b == ']':
        return True
    else:
        return False

for i in bracket:
    stack.append(i)
    while len(stack) >= 2:
        if matching(stack[-2], stack[-1]):
            stack.pop()
            stack.pop()
        else:
            break

'''
(()[[]])([])

2
(()[[]])
(2+(3*3))*2
'''

