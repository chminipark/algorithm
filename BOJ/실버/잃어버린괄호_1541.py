# import sys
# input = sys.stdin.readline

# s = input().strip()
# digit = []
# cnt = 0

# for i in range(len(s)):
#     if s[i] == '-':
#         digit.append(eval(s[cnt:i]))
#         cnt = i+1
# else:
#     digit.append(eval(s[cnt:]))

# if len(digit) == 1:
#     print(digit[0])
# else:
#     print(digit[0] - sum(digit[1:]))

## 왜안될까.. 반례가 뭘까..

import sys
input = sys.stdin.readline

s = list(map(str, input().strip().split('-')))

def plus(s: str):
    return sum(list(map(int, s.split('+'))))

if len(s) == 1:
    print(plus(s[0]))
else:
    print(plus(s[0]) - plus('+'.join(s[1:])))