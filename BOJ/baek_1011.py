import sys

T = int(sys.stdin.readline())
result = list()

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    h = y - x
    count, countplus, ish = 1, 1, 1
    brk = False
    while True:
        for i in range(2):
            if ish > h:
                brk = True
                result.append(count-1)
                break
            count += 1
            ish += countplus
        if brk:
            break
        countplus += 1

for i in result:
    print(i)