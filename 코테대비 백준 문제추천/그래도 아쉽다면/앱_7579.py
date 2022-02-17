import sys

def solution():
    sum_cost = sum(c_list)

    dp = [[0] * (sum_cost+1) for _ in range(n+1)]

    ans = sum_cost
    for i in range(1, n+1):
        for j in range(1, sum_cost+1):
            if j < c_list[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], m_list[i] + dp[i-1][j-c_list[i]])

            if dp[i][j] >= m:
                ans = min(ans, j)
    
    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    m_list = [0] + list(map(int, input().split()))
    c_list = [0] + list(map(int, input().split()))
    if m == 0:
        print(0)
        sys.exit()
    solution()






'''
5 60
30 10 20 35 40
3 0 3 5 4

    0   1   2   3   4   5   
1      3   3
2
3
4
5






'''
