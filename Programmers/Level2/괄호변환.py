def solution(p):
    answer = ''

    # 균형잡힌 괄호 판단하기
    def isbalanced_sentence(s):
        if  s.count('(') == s.count(')'):
            return True
        else:
            return False

    # 2 문자열 분리
    def separate(w):
        nonlocal u, v
        for i in range(1, len(w), 2):
            if balanced_sentence(w[:i+1]):
                u = w[:i+1]
                if i+1 == len(w):
                    v = ''
                else:
                    v = w[i+1:]
                return

    # 올바른 문자열 판단하기
    def iscorrect_sentence(s):
        stack = []

        for i in s:
            stack.append(i)
            if stack and len(stack) >= 2:
                if stack[-1] == ')' and stack[-2] == '(':
                    stack.pop()
                    stack.pop()
        
        if not stack:
            return True
        else:
            return False

    def recursive():
        

    ## -- 실행부분
    u, v = '', ''
    # 1
    if p == '':
        return ''
    # 2
    separate(p)

    # 3
    if iscorrect_sentence(u):
        # 1
        if v == '':
            return ''
        # 2
        separate(v)


    # 4 올바른 문자열로 바꾸기
    def change_correct_sentence():
        # 4-1
        return_str = '('
        # 4-2
        v

        #4-3







    return answer

s = [1,2,3]