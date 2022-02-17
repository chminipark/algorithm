import sys

def dfs(a,b,c,prev):
    if [a,b,c] == cnt:
        print(''.join(ans))
        sys.exit()
    
    if memo[a][b][c][prev[0]][prev[1]]:
        return False
    memo[a][b][c][prev[0]][prev[1]] = True

    if a+1 <= cnt[A]:
        ans[a+b+c] = 'A'
        if dfs(a+1, b, c, [prev[1], A]):
            return True
    
    if b+1 <= cnt[B]:
        ans[a+b+c] = 'B'
        if prev[1] != B:
            if dfs(a, b+1, c, [prev[1], B]):
                return True
    
    if c+1 <= cnt[C]:
        ans[a+b+c] = 'C'
        if prev[0] != C and prev[1] != C:
            if dfs(a, b, c+1, [prev[1], C]):
                return True
    
    return False


if __name__ == '__main__':
    input = sys.stdin.readline  
    A, B, C = 0, 1, 2
    s = input().rstrip()
    len_s = len(s)
    cnt = [s.count(w) for w in 'ABC']
    ans = [''] * (len_s)
    memo = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(len_s)] for _ in range(len_s)] for _ in range(len_s)]
    dfs(0, 0, 0, [0,0])
    print(-1)