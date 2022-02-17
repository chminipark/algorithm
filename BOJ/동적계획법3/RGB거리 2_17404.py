# import sys

# input = sys.stdin.readline

# n = int(input())
# rgb = [list(map(int, input().split())) for _ in range(n)]
# inf = sys.maxsize
# dp = [[0] * (3) for _ in range(n)]

# ans = inf
# for first in range(3):
#     for i in range(3):
#         if first == i:
#             dp[0][i] = rgb[0][i]
#         else:
#             dp[0][i] = inf

#     for i in range(1,n):
#         dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
#         dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
#         dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]
    
#     for i in range(3):
#         if first == i:
#             continue
#         ans = min(dp[n-1][i], ans)

# print(ans)








import sys

def solution():
    dp = [[0]*3 for _ in range(n)]
    inf = sys.maxsize
    ans = inf

    for first in range(3):
        for i in range(3):
            if first == i:
                dp[0][i] = rgb_list[0][i]
            else:
                dp[0][i] = inf
        
        for i in range(1,n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb_list[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb_list[i][1]
            dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + rgb_list[i][2]
        
        for i in range(3):
            if first == i:
                continue
            ans = min(dp[n-1][i], ans)
    
    print(ans)
            
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    rgb_list = [list(map(int, input().split())) for _ in range(n)]
    solution()