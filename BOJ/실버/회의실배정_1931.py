import sys
input = sys.stdin.readline

N = int(input())
M = []

for _ in range(N):
    M.append(list(map(int, input().split())))

M = sorted(M, key=lambda x:x[0])
M = sorted(M, key=lambda x:x[1])

ans = []
ans.append(M[0])

for i in range(1,len(M)):
    if ans[-1][1] <= M[i][0]:
        ans.append(M[i])

print(len(ans))

