import itertools
import sys
input = sys.stdin.readline

N = int(input())
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))

answer = [0,0,0]

def cut(matrix: list):

    check = matrix[0][0]
    ischeck = True
    for i in matrix:
        for j in i:
            if j != check:
                ischeck = False
                break
        if not ischeck:
            break

    if ischeck:
        answer[check+1] += 1
        return
    elif len(matrix)//3 == 1:
        for i in matrix:
            for j in i:
                answer[j+1] += 1
        return
    else:
        n = len(matrix)//3
        for i, j in itertools.product([0, n, n*2], repeat=2):
            cut(slicing(matrix, n, i, j))

def slicing(m, n, i ,j):
    sliced = []
    for y in m[j:j+n]:
        sliced.append(y[i:i+n])
    return sliced

cut(m)
for i in answer:
    print(i)