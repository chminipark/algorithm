from collections import deque

s = int(input())

q = deque()
q.append((1,0))
# (emoji, clip)

dp = [[-1]*(s+1) for _ in range(s+1)]
dp[1][0] = 0
while q:
    e, c = q.popleft()
    if dp[e][e] == -1:
        dp[e][e] = dp[e][c] + 1
        q.append((e,e))
    if e+c <= s and dp[e+c][c] == -1:
        dp[e+c][c] = dp[e][c] + 1
        q.append((e+c, c))
    if 0 <= e-1 and dp[e-1][c] == -1:
        dp[e-1][c] = dp[e][c] + 1
        q.append((e-1, c))

ans = float('inf')
for i in range(s+1):
    if dp[s][i] != -1:
        ans = min(ans, dp[s][i])
print(ans)


# from collections import deque
# n = int(input())
# dist = [[-1]* (n+1) for _ in range(n+1)]
# q = deque()
# q.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
# dist[1][0] = 0
# while q:
#     s,c = q.popleft()
#     if dist[s][s] == -1: # 방문하지 않았으면
#         dist[s][s] = dist[s][c] + 1
#         q.append((s,s))
#     if s+c <= n and dist[s+c][c] == -1:
#         dist[s+c][c] = dist[s][c] + 1
#         q.append((s+c, c))
#     if s-1 >= 0 and dist[s-1][c] == -1:
#         dist[s-1][c] = dist[s][c] + 1
#         q.append((s-1, c))
# answer = -1
# for i in range(n+1):
#     if dist[n][i] != -1:
#         if answer == -1 or answer > dist[n][i]:
#             answer = dist[n][i]
# print(answer)

# for i in dist:
#     print(i)