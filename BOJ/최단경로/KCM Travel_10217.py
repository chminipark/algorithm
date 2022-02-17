import sys
import math

input = sys.stdin.readline

answer = []
def solution():
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append((v,c,d))

    dp = [[math.inf] * (m+1) for _ in range(n+1)]
    dp[1][0] = 0
    for money in range(m+1):
        for vertex in range(1,n+1):
            if dp[vertex][money] != math.inf:
                for v, c, d in graph[vertex]:
                    if money + c <= m:
                        dp[v][money+c] = min(dp[v][money+c], dp[vertex][money] + d)
    
    ans = min(dp[-1])
    if ans == math.inf:
        answer.append('Poor KCM')
    else:
        answer.append(ans)

t = int(input())

for _ in range(t):
    solution()

for i in answer:
    print(i)