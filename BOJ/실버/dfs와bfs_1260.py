# import collections
# import sys
# input = sys.stdin.readline

# n, m, v = map(int, input().split())
# graph_list = [list(map(int, input().strip().split())) for _ in range(m)]
# graph = dict()

# for i in set(sum(graph_list, [])):
#     graph[i] = set()

# for x,y in graph_list:
#     graph[x].add(y)
#     graph[y].add(x)

# def bfs(start):
#     visited = []
#     q = collections.deque([start])

#     while q:
#         node = q.popleft()
#         if node not in visited:
#             visited.append(node)
#             q.extend(sorted(list(graph[node])))
    
#     return visited

# def dfs(start):
#     visited = []
#     stack = [start]

#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.append(node)
#             stack.extend(sorted(list(graph[node]), reverse= True))

#     return visited

# print(' '.join(map(str, dfs(v))))
# print(' '.join(map(str, bfs(v))))

## 런타임에러...
import collections
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(start_node, visited = []):
    visited.append(start_node)
    print(start_node, end=' ')

    for i in range(len(graph[start_node])):
        if graph[start_node][i] == 1 and i not in visited:
            dfs(i, visited)

def bfs(start_node):
    visited = [start_node]
    q = collections.deque([start_node])

    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in range(len(graph[start_node])):
            if graph[node][i] == 1 and i not in visited:
                q.append(i)
                visited.append(i)

dfs(v)
print('')
bfs(v)