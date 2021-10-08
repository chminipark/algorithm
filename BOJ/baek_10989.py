import sys

N = int(sys.stdin.readline())
cntList = [0]*10001

for _ in range(N):
    cntList[int(sys.stdin.readline())] += 1

for i in range(len(cntList)):
    if cntList[i] != 0:
        for _ in range(cntList[i]):
            print(i)