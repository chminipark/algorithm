graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','G','H'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}

import collections

def bfs(graph, start_node):
    visited = []
    queue = collections.deque(start_node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    
    return visited

def dfs_iteration(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    
    return visited

print(dfs_iteration(graph, 'A'))