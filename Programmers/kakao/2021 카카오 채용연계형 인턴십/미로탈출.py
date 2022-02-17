import heapq

def getNextBit(nex_node, cur_bit, traps_dic):
    if nex_node in traps_dic:
        return cur_bit ^ (1 << traps_dic[nex_node])
    return cur_bit

def isTrap(cur_node, nex_node, cur_bit, traps_dic):
    cur_state, nex_state = False, False
    if cur_node in traps_dic:
        cur_state = (cur_bit & (1 << traps_dic[cur_node])) > 0
    if nex_node in traps_dic:
        nex_state = (cur_bit & (1 << traps_dic[nex_node])) > 0
    return cur_state != nex_state

def solution(n, start, end, roads, traps):
    graph = [[] for _ in range(n+1)]
    for a,b,c in roads:
        # [nex_node, dist, isTrap]
        graph[a].append([b, c, False])
        graph[b].append([a, c, True])
    
    traps_dic = { v:i for i, v, in enumerate(traps) }
    distance = [[float('inf') for _ in range(n+1)] for _ in range(1 << len(traps))]
    distance[0][start] = 0
    hq = []
    # [cur_dist, cur_node, cur_bit]
    heapq.heappush(hq, [0, start, 0])

    ans = float('inf')
    while hq:
        cur_dist, cur_node, cur_bit = heapq.heappop(hq)

        if cur_node == end:
            ans = min(ans, cur_dist)
            continue

        if distance[cur_bit][cur_node] < cur_dist:
            continue

        for nex_node, dist, is_trap in graph[cur_node]:
            if is_trap != isTrap(cur_node, nex_node, cur_bit, traps_dic):
                continue

            nex_dist = dist + cur_dist
            nex_bit = getNextBit(nex_node, cur_bit, traps_dic)

            if nex_dist < distance[nex_bit][nex_node]:
                distance[nex_bit][nex_node] = nex_dist
                heapq.heappush(hq, [nex_dist, nex_node, nex_bit])
    
    return ans


solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])

'''
4	1	4	[[1, 2, 1], [3, 2, 1], [2, 4, 1]]	[2, 3]	
'''