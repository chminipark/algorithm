import sys

N = int(sys.stdin.readline())

starList = [[0 for i in range(N)] for i in range(N)]
starList[0][0:3] = starList[2][0:3] = [1, 1, 1]
starList[1][0:3] = [1, 0, 1]

def star(n):
    global starList
    if n == 3:
        return
    a = n//3
    star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for h in range(a):
                starList[(i*a)+h][(j*a):(j*a)+a] = starList[h][:a]

star(N)
for i in starList:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print('')


# https://study-all-night.tistory.com/5