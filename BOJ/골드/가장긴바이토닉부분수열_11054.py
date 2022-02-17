import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a_list[i] > a_list[j]:
            increase[i] = max(increase[i], increase[j]+1)

for i in reversed(range(n)):
    for j in range(n-i-1):
        if a_list[i] > a_list[n-j-1]:
            decrease[i] = max(decrease[i], decrease[n-j-1]+1) 

result = []
for x,y in zip(increase, decrease):
    result.append(x+y-1)

print(max(result))

