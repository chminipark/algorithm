import sys
input = sys.stdin.readline

N = int(input())
P = []

P = list(map(int, input().split()))

P.sort()

ans = 0
ans_list = []

for i in P:
    ans += i
    ans_list.append(ans)
    
print(sum(ans_list))