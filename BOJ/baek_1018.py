N, M = map(int, input().split())

chessList = list()
board = list()

for _ in range(N):
    chessList.append(input())

result = 64
def check(a: int, b: int, isb: bool):
    global chessList, result
    count = 0
    if isb:
        isB = True
        isW = False
    else:
        isB = False
        isW = True
    for i in range(8):
        for j in chessList[a+i][b:b+8]:
            if isB:
                isB = False
                isW = True
                if j != 'B':
                    count += 1
                continue
            if isW:
                isW = False
                isB = True
                if j != 'W':
                    count += 1
        isB = not isB       
        isW = not isW
    if count <= result:
        result = count

for i in range(N-7):
    for j in range(M-7):
        check(i, j, True)

for i in range(N-7):
    for j in range(M-7):
        check(i, j, False)

print(result)