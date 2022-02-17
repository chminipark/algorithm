import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

inf = sys.maxsize
dist = [inf] * (n+1)
def bf(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            wei = edges[j][2]

            next_wei = wei + dist[cur_node]

            if dist[cur_node] != inf and dist[next_node] > next_wei:
                dist[next_node] = next_wei

                if i == n-1:
                    return True
    
    return False

isrecycle = bf(1)

if isrecycle:
    print(-1)
else:
    for i in range(2, n+1):
        print(-1 if dist[i] == inf else dist[i])