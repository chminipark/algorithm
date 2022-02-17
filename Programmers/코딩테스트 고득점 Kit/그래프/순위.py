def solution(n, results):
    memo = [[None] * (n) for _ in range(n)]
    for a, b in results:
        memo[a-1][b-1] = True
        memo[b-1][a-1] = False
    

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if memo[i][j] == None:
                    continue
                if memo[i][j] == memo[j][k]:
                    memo[i][k] = memo[i][j]
                    memo[k][i] = not memo[i][j]

    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if memo[i][j] == None:
                cnt += 1
        if cnt == 1:
            ans += 1

    return ans

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])