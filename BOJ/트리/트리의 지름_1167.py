import sys

def dfs_stack(node):
    # (node, dist)
    stack = [(node, 0)]
    dist = [0] * (v+1)
    dist[node] = -1

    max_node, max_dist = node, 0
    while stack:
        cur_node, cur_dist = stack.pop()

        for nex_node, nex_dist in tree[cur_node]:
            if dist[nex_node] == 0:
                dist[nex_node] = cur_dist + nex_dist
                if max_dist < dist[nex_node]:
                    max_node = nex_node
                    max_dist = dist[nex_node]
                stack.append((nex_node, dist[nex_node]))
    
    return (max_node, max_dist)


if __name__ == '__main__':
    input = sys.stdin.readline
    v = int(input())
    tree = [[] for _ in range(v+1)]
    for _ in range(v):
        tmp = list(map(int, input().split()))
        node = tmp[0]
        for j in range(1, len(tmp)-2, 2):
            tree[node].append((tmp[j], tmp[j+1]))
            # (node, dist)
    
    first = dfs_stack(1)
    second = dfs_stack(first[0])
    print(second[1])