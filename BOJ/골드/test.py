import sys
input = sys.stdin.readline

ans = []
while True:
    t = list(map(int, input().split()))
    if t == [0]:
        break
    max_t = len(t)
    for i in range(len(t)):
        j = i+1
        while True:
            if j == len(t):
                break
            if 

