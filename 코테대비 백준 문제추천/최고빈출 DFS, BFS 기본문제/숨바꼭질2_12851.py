# from collections import deque

# n, k = map(int, input().split())
# dp = [[-1,0] for _ in range(100001)]

# q = deque()
# q.append(n)
# dp[n][0] = 0
# dp[n][1] = 1

# while q:
#     cur = q.popleft()

#     for nex in [cur+1, cur-1, cur*2]:
#         if 0 <= nex <= 100000:
#             if dp[nex][0] == -1:
#                 dp[nex][0] = dp[cur][0] + 1
#                 dp[nex][1] = dp[cur][1]
#                 q.append(nex)
#             elif dp[nex][0] == dp[cur][0] + 1:
#                 dp[nex][1] += dp[cur][1]

# print(dp[k][0])
# print(dp[k][1])



from collections import deque
import sys

n, k = map(int, input().split())

def bfs():
    # [time, cnt]
    memo = [[-1,0] for _ in range(100001)]
    memo[n][0] = 0
    memo[n][1] = 1

    q = deque()
    q.append(n)
    
    while q:
        cur_num = q.popleft()

        for nex_num in [cur_num+1, cur_num-1, cur_num*2]:
            if 0 <= nex_num <= 100000:
                if memo[nex_num][0] == -1:
                    memo[nex_num][0] = memo[cur_num][0] + 1
                    memo[nex_num][1] = memo[cur_num][1]
                    q.append(nex_num)
                elif memo[nex_num][0] == memo[cur_num][0] + 1:
                    memo[nex_num][1] += memo[cur_num][1] 
    
    return memo[k]

print(*bfs(), sep='\n')

