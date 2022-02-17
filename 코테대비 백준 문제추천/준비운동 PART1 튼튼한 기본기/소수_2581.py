import math

m = int(input())
n = int(input())

memo = [True] * (n+1)
memo[0], memo[1] = False, False

for i in range(2, int(math.sqrt(n))+1):
    j = 2
    while i*j <= n:
        memo[i*j] = False
        j += 1

sum_prime = 0
min_prime = -1
for i in reversed(range(m, n+1)):
    if memo[i]:
        sum_prime += i
        min_prime = i

if sum_prime == 0:
    print(-1)
else:
    print(sum_prime)
    print(min_prime)