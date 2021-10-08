import sys

primeList = [True for i in range(10001)]
primeList[0] = False
primeList[1] = False
resultList = list()

for i in range(2, int(len(primeList)/2)+1):
    if primeList[i]:
        for j in range(i*2, len(primeList), i):
            primeList[j] = False

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    a = int(n/2)
    b = n-a

    while True:
        if primeList[a] and primeList[b]:
            resultList.append([b,a])
            break
        a += 1
        b -= 1

for x, y in resultList:
    print(x, y)

# 에라토스테네스 체