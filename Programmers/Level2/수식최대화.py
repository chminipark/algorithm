import itertools
def solution(expression):
    answer = 0

    operator = ['+','-','*']
    digit = []
    cnt = 0

    # 숫자, 연산자 분리
    for i in range(len(expression)):
        if expression[i].isdigit():
            cnt += 1
        else:
            digit.append(''.join(expression[i-cnt:i]))
            cnt = 0
    else:
        digit.append(''.join(expression[len(expression)-cnt:len(expression)]))
            
    






import collections
expression = "100-200*300-500+20"
list(expression)
print(expression[2:])
q = collections.deque(expression)


