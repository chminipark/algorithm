p = [0]*101
p[1] = 1
p[2] = 1
p[3] = 1
p[4] = 2
p[5] = 2
p[6] = 3

def pn(n: int):
    global last_n
    if p[n]:
        return p[n]
    for i in range(last_n, n+1):
        p[i] = p[i-5] + p[i-1]
    last_n = n
    return p[n]

import sys
input = sys.stdin.readline

t = int(input())
n_list = []

for _ in range(t):
    n_list.append(int(input()))

last_n = 7
for i in n_list:
    print(pn(i))