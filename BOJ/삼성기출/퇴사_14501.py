import sys
input = sys.stdin.readline

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

answer = 0
def solution(n_list, idx):
    t, p = n_list[0][0], n_list[0][1]
    if idx + t + 1 > n:
        return
    else:
        



