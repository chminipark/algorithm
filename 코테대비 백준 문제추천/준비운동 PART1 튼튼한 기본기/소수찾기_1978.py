import sys
import math

input = sys.stdin.readline

def isprime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

N = int(input())
ans = 0
for i in list(map(int, input().split())):
    if isprime(i):
        ans += 1

print(ans)