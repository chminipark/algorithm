# def solution(name):
#     A = 'A'*len(name)
#     remove_name = name
#     currentIndex = 0
#     answer = 0

#     def pickAlphabet(a):
#         nonlocal answer
#         # alphabet = 'ABCDEFGHIJKLNMOPQRSTUVWXYZ'
#         left = 'BCDEFGHIJKLN'
#         right = 'OPQRSTUVWXYZ'
#         reversed_right = right[::-1]
#         if a == 'M':
#             # return 13
#             answer += 13
#         elif a == 'A':
#             # return 0
#             answer += 0
#         elif a in left:
#             # return left.find(a)+1
#             answer += left.find(a)+1
#         else:
#             # return reversed_right.find(a)+1
#             answer += reversed_right.find(a)+1
#         # remove_name 지우기, A 업데이트

#     def moveCursor(a):
#         nonlocal currentIndex
#         nonlocal answer
#         # reversed_a = a[::-1]
#         moveright = 0
#         moveleft = 0
#         while 1:
#             moveright += 1
#             if a[currentIndex+moveright] != 'A':
#                 break
#         while 1:
#             moveleft += 1
#             if a[currentIndex-moveleft] != 'A':
#                 break
#         if moveright > moveleft:
#             currentIndex = currentIndex-moveleft
#             answer += moveleft
#         elif moveright <= moveleft:
#             currentIndex = currentIndex+moveright
#             answer += moveright
    
#     while A != name:
#         moveCursor(remove_name)
#         # remove_alpha = remove_name[currentIndex]
#         # remove_index = currentIndex
#         pickAlphabet(remove_name[currentIndex])
#         A[currentIndex] = remove_name[currentIndex]
#         remove_name[currentIndex] = 'A'
    
#     return answer


# sol = solution('JAN')
# print(sol)

def solution(name):
    answer = 0
    return answer

ABCDEFGHIJKLN M OPQRSTUVWXYZ