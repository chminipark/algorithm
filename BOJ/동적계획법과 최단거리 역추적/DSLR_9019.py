import collections
import sys

input = sys.stdin.readline
    
def DSLR(a, b):
    q = collections.deque()
    visited = [[] for _ in range(10000)]
    q.append(a)

    while q:
        if visited[b]:
            break

        now = q.popleft()

        # D
        D = now % 10000 if now*2 > 9999 else now * 2
        if not visited[D]:
            visited[D] = [now, 'D']
            q.append(D)
        
        # S
        S = 9999 if now == 0 else now - 1
        if not visited[S]:
            visited[S] = [now, 'S']
            q.append(S)
        

        # L
        front = now % 1000
        back = now // 1000
        L = front*10 + back
        if not visited[L]:
            visited[L] = [now, 'L']
            q.append(L)
        
        # R
        front = now % 10
        back = now // 10
        R = front*1000 + back
        if not visited[R]:
            visited[R] = [now, 'R']
            q.append(R)


        # # L
        # templ = collections.deque(str(now))
        # templ.rotate(-1)
        # L = int(''.join(templ))
        # if not visited[L]:
        #     visited[L] = [now, 'L']
        #     q.append(L)
        
        # # R
        # tempr = collections.deque(str(now))
        # tempr.rotate(1)
        # R = int(''.join(tempr))
        # if not visited[R]:
        #     visited[R] = [now, 'R']
        #     q.append(R)
        
    ans = ''
    idx = b
    while True:
        ans = visited[idx][1] + ans
        if visited[idx][0] == a:
            break
        idx = visited[idx][0]
    
    return ans

t = int(input())
answer = []
for _ in range(t):
    a, b = map(int, input().split())
    answer.append(DSLR(a, b))

print(*answer, sep='\n')

# '''

# visited = (num, DSLR)
# visited[num*2] = (num, DSLR)
# q.append(num*2)

# '''



## DP로.....

# import sys

# input = sys.stdin.readline

# def DSLR(a, b):
#     dist = [0] * 10000
#     path = [0] * 10000

#     for i in range(10000):
#         # D
#         D = now % 10000 if now*2 > 9999 else now * 2
#         if not visited[D]:
#             visited[D] = [now, 'D']
#             q.append(D)
        
#         # S
#         S = 9999 if now == 0 else now - 1
#         if not visited[S]:
#             visited[S] = [now, 'S']
#             q.append(S)
        
#         # L
#         templ = collections.deque(str(now))
#         templ.rotate(-1)
#         L = int(''.join(templ))
#         if not visited[L]:
#             visited[L] = [now, 'L']
#             q.append(L)
        
#         # R
#         tempr = collections.deque(str(now))
#         tempr.rotate(1)
#         R = int(''.join(tempr))
#         if not visited[R]:
#             visited[R] = [now, 'R']
#             q.append(R)
