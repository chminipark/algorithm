import sys

def solution(num_list, ques):

    dp = [[0] * (n) for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for j in range(1, n):
        for i in range(j-1, -1, -1):
            if num_list[i] != num_list[j]:
                dp[i][j] = 0
                continue
            start, end = i+1, j-1
            if start >= end:
                dp[i][j] = 1
                continue
            if dp[start][end] == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
    
    for i in ques:
        print(dp[i[0]-1][i[1]-1], sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    n_list = list(map(int, input().split()))
    q = int(input())
    q_list = []
    for _ in range(q):
        a, b = map(int, input().split())
        q_list.append((a,b))
    solution(n_list, q_list)




'''
    1   2   1   3   1   2   1
1   1   0   1   0
2       1   0   0   0
1           1   0   1
3               1   0
1                   1
2
1

'''