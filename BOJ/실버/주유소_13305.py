import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
gas = list(map(int, input().split()))

min_gas = gas[0]
min_cost = (gas[0] * road[0])

for i in range(1, len(road)):
    if min_gas > gas[i]:
        min_cost += gas[i] * road[i]
        min_gas = gas[i]
    else:
        min_cost += min_gas * road[i]

print(min_cost)