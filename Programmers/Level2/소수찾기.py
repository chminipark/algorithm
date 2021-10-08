import math
import itertools

def solution(numbers):
    answer = set()

    def isprime(n: int):
        if n == 0 or n == 1:
            return

        nonlocal answer
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return
        else:
            answer.add(n)
            return

    for i in range(1,len(numbers)+1):
        for j in itertools.permutations(numbers,i):
            isprime(int(''.join(j)))

    return len(answer)


n = '011'
solution(n)

