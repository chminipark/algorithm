h, w = map(int, input().split())
rain = list(map(int, input().split()))

block = [[0 for _ in range(w)] for _ in range(h)]

for i in range(w):
    for j in range(h-1, (h-1)-rain[i], -1):
        block[j][i] = 1

ans = 0

for i in range(h):
    one = [j for j in range(len(block[i])) if block[i][j] == 1]
    for i in range(len(one)-1):
        ans += (one[i+1] - one[i]) - 1

print(ans)
            







'''
4 4
3 0 1 4

'''