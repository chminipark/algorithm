from collections import defaultdict

# 2
def separate(w):
    check = defaultdict(int)
    idx = 0
    for i in range(0, len(w), 2):
        check[w[i]] += 1
        check[w[i+1]] += 1
        if len(check) == 2 and check['('] == check[')']:
            idx = i+1
            break

    a, b = '', ''
    if idx == len(w)-1:
        a = w
    else:
        a = w[:idx+1]
        b = w[idx+1:]
    
    return (a,b)

def isCorrect(w):
    stack = []
    for i in w:
        stack.append(i)
        while len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()
    if stack:
        return False
    return True
    
def recursion(w):
    if not w:
        return w

    u, v = separate(w)
    if isCorrect(u):
        return u + recursion(v)
    else:
        tmp_v = recursion(v)
        tmp_v = '(' + tmp_v + ')'
        tmp_u = reverse_w(u[1:-1])
        return tmp_v + tmp_u

def reverse_w(w):
    return ''.join(map(lambda x: ')' if x == '(' else '(', w))

def solution(p):
    # 1
    if not p:
        return ''
    
    if isCorrect(p):
        return p
    
    return recursion(p)
    # print(recursion(p))
    


# solution(")(")
# solution("()))((()")