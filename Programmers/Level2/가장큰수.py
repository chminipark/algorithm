# 시간초과....
"""
import itertools

def solution(numbers):
    permu = []
    numbers_int = list(map(str, numbers))

    for i in itertools.permutations(numbers_int, len(numbers_int)):
        permu.append(int(''.join(i)))

    return str(max(permu))


print(solution(numbers))

import itertools
numbers = list(map(str, [6, 10, 2]))

a = []

for i in itertools.permutations(numbers, len(numbers)):
    print(int(''.join(i)))
"""

def solution(numbers):
    answer = ''
    return answer







numbers = [3, 30, 34, 5, 9]

for i in range(len(numbers)):
    numbers[i] = (numbers[i], numbers[i]//ten(numbers[i]))


def ten(n: int):
    digit = '0' * len(str(n))
    digit = digit.replace('0', '1', 1)
    return int(digit)

ten(30)

digit = '0'*len(str(30))
digit[0] = '1'