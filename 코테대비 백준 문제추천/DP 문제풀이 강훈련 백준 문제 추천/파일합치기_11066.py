import sys

def solution(book):
    ans = 0
    dp = [[0] * (len(book)) for _ in range(len(book))]
    for j in range(1, len(book)):
        for i in range(j-1, -1, -1):
            min_value = sys.maxsize
            for k in range(j-i):
                min_value = min(min_value, dp[i][i+k] + dp[i+k+1][j])
            dp[i][j] = min_value + sum(book[i:j+1])
    return dp[0][-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    ans = []
    t = int(input())
    for _ in range(t):
        k = int(input())
        k_list = list(map(int, input().split()))
        ans.append(solution(k_list))
    print(*ans, sep='\n')