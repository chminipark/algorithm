import sys

input = sys.stdin.readline

T = int(input())

def solution(case: list):
    return sorted(case)[7]

ans = []
for _ in range(T):
    ans.append(solution(list(map(int, input().split()))))

for i in ans:
    print(i)
