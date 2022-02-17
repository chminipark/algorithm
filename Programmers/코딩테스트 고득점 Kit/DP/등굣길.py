# def solution(m, n, puddles):
#     from collections import deque

#     memo = [[float('inf')] * (m) for _ in range(n)]
#     for y,x in puddles:
#         memo[x-1][y-1] = -1
    
#     q = deque()
#     # [[좌표],카운트]
#     q.append([[0,0],0])

#     ans = 0
#     while q:
#         cur_cordi, cur_cnt = q.popleft()
#         cur_y, cur_x = cur_cordi

#         for y, x in [(1,0), (0,1)]:
#             nex_y = y + cur_y
#             nex_x = x + cur_x

#             if nex_x == m-1 and nex_y == n-1:
#                 if memo[-1][-1] >= cur_cnt:
#                     if memo[-1][-1] == cur_cnt:
#                         ans += 1
#                     else:
#                         ans = 1
#                     memo[-1][-1] = cur_cnt
#                 continue

#             if 0 <= nex_y < n and 0 <= nex_x < m:
#                 if memo[nex_y][nex_x] != -1:
#                     if memo[nex_y][nex_x] >= cur_cnt+1:
#                         memo[nex_y][nex_x] = cur_cnt+1
#                         q.append([[nex_y, nex_x], cur_cnt])
    
#     return ans


def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1: continue
            if [j,i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
                
    return dp[n][m]

                    
