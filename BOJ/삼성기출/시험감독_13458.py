import sys
import math
import functools
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
b, c = map(int, input().split())

a_list[0] = math.ceil((a_list[0]-b)/c)+1 if a_list[0]-b>0 else 1

def solution(x, y):
    # x = math.ceil((x-b)/c)+1 if x-b>0 else 1
    y = math.ceil((y-b)/c)+1 if y-b>0 else 1
    return x + y

answer = functools.reduce(solution, a_list)

print(answer)
        

# answer = list(map(lambda x: math.ceil((x-b)/c)+1 if x-b > 0 else 1, a_list))
# print(sum(answer))
