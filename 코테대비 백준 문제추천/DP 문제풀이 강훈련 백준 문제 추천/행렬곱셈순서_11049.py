import sys

def solution(matrix):
    ans = 0

    inf = sys.maxsize
    dp = [[inf] * (len(matrix)) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        dp[i][i] = 0
    for j in range(1, len(matrix)):
        for i in range(j-1, -1, -1):
            for k in range(j-i):
                dp[i][j] = min(dp[i][j], dp[i][i+k] + dp[i+k+1][j] + (matrix[i][0]*matrix[i+k][1]*matrix[j][1]))
                
    print(dp[0][-1])

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    n_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        n_list.append((a,b))
    solution(n_list)



'''
3
5 3
3 2
2 6



'''