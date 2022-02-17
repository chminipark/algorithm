import heapq
import sys

input = sys.stdin.readline

inf = sys.maxsize
def dij(start):
    heap = []
    heapq.heappush(heap, (0,start))
    dist = [inf] * (n+1)
    dist[start] = 0

    while heap:
        cur_wei, cur_node = heapq.heappop(heap)

        if dist[cur_node] < cur_wei:
            continue

        for wei, next_node in graph[cur_node]:
            next_wei = wei + cur_wei
            if dist[next_node] > next_wei:
                dist[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
    
    return dist

T = int(input())
answer = []
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))
    
    t_list = []
    for _ in range(t):
        t_list.append(int(input()))

    s_ = dij(s)
    g_ = dij(g)
    h_ = dij(h)

    ans = []
    for i in t_list:
        if s_[g] + g_[h] + h_[i] == s_[i] or s_[h] + h_[g] + g_[i] == s_[i]:
            ans.append(i)

    ans.sort()
    answer.append(ans)
    
for row in answer:
    for i in row:
        print(i, end=' ')
    print()