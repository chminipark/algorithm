import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
start_node, end_node = map(int, input().split())

inf = sys.maxsize
mst_list = [inf] * (n+1)
path_list = [[] for _ in range(n+1)]
def dij(start):
    q = []
    heapq.heappush(q, (0, start, [start]))
    # (cur_wei, start_node, [path])

    while q:
        cur_wei, cur_node, path = heapq.heappop(q)
        
        if cur_wei > mst_list[cur_node]:
            continue

        for next_node, next_wei in graph[cur_node]:
            dist = next_wei + cur_wei
            if dist < mst_list[next_node]:
                mst_list[next_node] = dist
                pathh = path + [next_node]
                path_list[next_node] = pathh
                heapq.heappush(q, (dist, next_node, pathh))

dij(start_node)
print(mst_list[end_node])
print(len(path_list[end_node]))
print(*path_list[end_node])