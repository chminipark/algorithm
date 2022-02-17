import itertools
import collections
import sys

input = sys.stdin.readline

n = int(input())
scv = sorted(list(map(int,input().split())) + [0]*(3-n), reverse = True)
q = collections.deque()
q.append((scv, 0))
visited = [[[False for _ in range(61)] for _ in range(61)] for _ in range(61)]
attack_case = list(itertools.permutations([9,3,1], 3))

while q:
    cur_scv, cur_cnt = q.popleft()

    if cur_scv[0] == 0:
        print(cur_cnt)
        break

    for case in attack_case:
        nex_scv_list = []
        for i in range(3):
            nex_scv = cur_scv[i] - case[i]
            nex_scv = 0 if nex_scv < 0 else nex_scv
            nex_scv_list.append(nex_scv)
        nex_scv_list.sort(reverse = True)

        if not visited[nex_scv_list[0]][nex_scv_list[1]][nex_scv_list[2]]:
            visited[nex_scv_list[0]][nex_scv_list[1]][nex_scv_list[2]] = True
            q.append((nex_scv_list, cur_cnt+1))
    

