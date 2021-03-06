# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


# def dfs(node, group):
#     visited[node] = group

#     for i in graph[node]:
#         if visited[i] == 0:
#             if not dfs(i, -group):
#                 return False
#         elif visited[node] == visited[i]:
#             return False
    
#     return True

# answer = []
# for _ in range(int(input())):
#     v, e = map(int, input().split())

#     graph = [[] for _ in range(v+1)]
#     visited = [0]*(v+1)
#     for _ in range(e):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
    
#     check = True
#     for i in range(1, v+1):
#         if visited[i] == 0:
#             check = dfs(i, 1)
#             if not check:
#                 break

#     answer.append('YES' if check else 'NO')

# for i in answer:
#     print(i)


import collections
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)] # 빈 그래프 생성
    visited = [0] * (V+1) # 방문한 정점 체크

    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b) # 무방향 그래프
        graph[b].append(a) # 무방향 그래프


    q = collections.deque()
    group = 1
    bipatite = True
    for i in range(1, V+1):
        if visited[i] == 0: # 방문하지 않은 정점이면 bfs 수행
            q.append(i)
            visited[i] = group
            while q:
                v = q.popleft()
                for w in graph[v]:
                    if visited[w] == 0: # 방문하지 않은 정점이면 큐에 삽입
                        q.append(w)
                        visited[w] = -1 * visited[v] # 현재 노드와 다른 그룹 지정
                    elif visited[v] == visited[w]: # 이미 방문한 경우, 동일한 그룹에 속하면 False
                        bipatite = False

    print('YES' if bipatite else 'NO')