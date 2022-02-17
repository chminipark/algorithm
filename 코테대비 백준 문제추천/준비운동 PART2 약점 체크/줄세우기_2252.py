import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_edge = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_edge[b] += 1

def solution():
    q = collections.deque()
    ans = []

    for i in range(1, n+1):
        if in_edge[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        ans.append(now)
        for next_node in graph[now]:
            in_edge[next_node] -= 1
            if in_edge[next_node] == 0:
                q.append(next_node)
    
    for i in ans:
        print(i, end= ' ')

solution()


# import sys
# import collections

# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# in_edge = [0] * (n+1)
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     in_edge[b] += 1

# def solution():
#     q = collections.deque()
#     ans = []

#     for i in range(1, n+1):
#         if in_edge[i] == 0:
#             q.append(i)
    
#     while q:
#         now = q.popleft()
#         ans.append(now)

#         for next_node in graph[now]:
#             in_edge[next_node] -= 1
#             if in_edge[next_node] == 0:
#                 q.append(next_node)
            
#     for i in ans:
#         print(i, end=' ')

# solution()