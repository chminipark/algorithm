def solution(number: str, k: int):
    stack = []

    for i in number:
        while stack and k != 0 and stack[-1] < int(i):
            stack.pop()
            k -= 1
        stack.append(int(i))

    if k != 0:
        stack = stack[:-k]

    return ''.join(list(map(str, stack)))
print(solution("4177252841", 4))

'''
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
'''

