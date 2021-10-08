# def solution(number, k):

#     stack = [number[0]]

#     for i in number[1:]:

#         while k>0 and stack[-1]<i and len(stack):
#             k -= 1
#             stack.pop()

#         stack.append(i)

#     if k != 0:
#         stack = stack[:-k]
#     return ''.join(stack)

# number = "1924"
# k = 2
# dicc = {}
# for i in range(len(number)):

# print(list(number))

def solution(number, k):
    stack = []

    for i in number:
        while stack and k != 0 and stack[-1] < int(i):
            stack.pop()
            k -= 1
        stack.append(int(i))

    if k != 0:
        stack = stack[:-k]

    return ''.join(list(map(str, stack)))



a = '1234'

a = [1,2,3,4]
''.join(a)

number = '1924'
for i in number:
    print(int(i))
k = 2

solution(number, k)
