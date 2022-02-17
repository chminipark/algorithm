import sys

def nexState(cur_cordi, cur_state):
    x, y = cur_cordi
    nex_state = cur_state[:]
    # 가로
    nex_state[x] |= (1 << n) - 1
    # 세로
    for i in range(n):
        nex_state[i] |= (1 << y)
    # 대각선
    for i in range(n):
        for dx, dy in [(-1,1), (1,1), (1,-1), (-1,-1)]:
            nex_x = x + (dx*i)
            nex_y = y + (dy*i)
            if 0 <= nex_x < n and 0 <= nex_y < n:
                nex_state[nex_x] |= (1 << nex_y)
    
    for i in nex_state:
        print(bin(i))
    print()
    return nex_state
    

def dfs():
    global ans

    if len(q_cordi) == n:
        ans += 1
        return
    
    for i in range(n):
        for j in range(n):
            cur_cordi = (i,j)
            cur_state = stack[-1][1] if stack else [(1 << n) for _ in range(n)]

            if cur_cordi in q_cordi:
                continue
            if cur_state[i] & (1 << j) != 0:
                continue
            
            q_cordi.add(cur_cordi)
            nex_state = nexState(cur_cordi, cur_state)
            stack.append([cur_cordi, nex_state])
            dfs()
            c, _ = stack.pop()
            q_cordi.remove(c)


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    # [[(cur_cordi), [cur_matri]]]
    stack = []
    q_cordi = set()
    ans = 0
    dfs()
    print(ans)
