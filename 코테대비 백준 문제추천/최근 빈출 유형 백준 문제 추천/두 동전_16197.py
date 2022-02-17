import sys
import collections

def bfs():
    q = collections.deque()
    q.append((coin[0], coin[1], 0))
    # coin1 기준 coin2 add
    memo = [[set() for _ in range(m)] for _ in range(n)]
    memo[coin[0][0]][coin[0][1]].add(coin[1])

    while q:
        coin1, coin2, cnt = q.popleft()
        
        if cnt > 10:
            print(-1)
            return

        for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
            nex_coin1 = (coin1[0] + x, coin1[1] + y)
            nex_coin2 = (coin2[0] + x, coin2[1] + y)

            if 0 <= nex_coin1[0] < n and 0 <= nex_coin1[1] < m:
                if board[nex_coin1[0]][nex_coin1[1]] == '#':
                    nex_coin1 = coin1
            else:
                nex_coin1 = (-1,-1)
            if 0 <= nex_coin2[0] < n and 0 <= nex_coin2[1] < m:
                if board[nex_coin2[0]][nex_coin2[1]] == '#':
                    nex_coin2 = coin2
            else:
                nex_coin2 = (-1,-1)
            
            if nex_coin1 == (-1,-1) and nex_coin2 != (-1,-1):
                if cnt+1 <= 10:
                    print(cnt+1)
                    return
            
            if nex_coin2 == (-1,-1) and nex_coin1 != (-1,-1):
                if cnt+1 <= 10:
                    print(cnt+1)
                    return
            
            if nex_coin1 != (-1,-1) and nex_coin2 != (-1,-1):
                if nex_coin2 not in memo[nex_coin1[0]][nex_coin1[1]]:
                    memo[nex_coin1[0]][nex_coin1[1]].add(nex_coin2)
                    q.append((nex_coin1, nex_coin2, cnt+1))

    print(-1)


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = []
    coin = []
    for i in range(n):
        row = list(input().strip())
        board.append(row)
        for j in range(m):
            if row[j] == 'o':
                coin.append((i,j))
    bfs()