import sys

input = sys.stdin.readline

n = int(input())
candy = [list(input().strip()) for _ in range(n)]

## 완탐 ##

def check(hORv, x, y, word):
    cnt = 0
    if hORv == True:
        j = y - 1
        while 0 <= j:
            if word == candy[x][j]:
                j -= 1
                cnt += 1
            else:
                break
        j = y + 1
        while j < n:
            if word == candy[x][j]:
                j += 1
                cnt += 1
            else:
                break
    else:
        i = x - 1
        while 0 <= i:
            if word == candy[i][y]:
                i -= 1
                cnt += 1
            else:
                break
        i = x + 1
        while i < n:
            if word == candy[i][y]:
                i += 1
                cnt += 1
            else:
                break
        
    return cnt + 1

def hori(h, a, b):
    if b >= n:
        return 1
    w1 = candy[h][a]
    w2 = candy[h][b]
    cnt = max(check(False, h, a, w2), check(False, h, b, w1))
    candy[h][b] = w1
    candy[h][a] = w2
    cnt = max(cnt, check(True, h, b, candy[h][b]))
    cnt = max(cnt, check(True, h, a, candy[h][a]))
    candy[h][a] = w1
    candy[h][b] = w2
    return cnt

def verti(v, a, b):
    if b >= n:
        return 1
    w1 = candy[a][v]
    w2 = candy[b][v]
    cnt = max(check(True, a, v, w2), check(True, b, v, w1))
    candy[b][v] = w1
    candy[a][v] = w2
    cnt = max(cnt, check(False, b, v, candy[b][v]))
    cnt = max(cnt, check(False, a, v, candy[a][v]))
    candy[a][v] = w1
    candy[b][v] = w2
    return cnt


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, hori(i, j, j+1))
        ans = max(ans, verti(i, j, j+1))

print(ans)