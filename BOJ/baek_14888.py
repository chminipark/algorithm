import sys
import itertools
import collections

_input = sys.stdin.readline

n = int(_input())
a_list = list(map(str, _input().split()))
o = list(map(int, _input().split()))

o_list = []
o_list += ['+'] * o[0]
o_list += ['-'] * o[1]
o_list += ['*'] * o[2]
o_list += ['//'] * o[3]

o_permu = set()

for i in itertools.permutations(o_list, len(o_list)):
    o_permu.add(i)

o_permu = list(o_permu)

def solution(a_list, o_list):
    q_a_list = collections.deque(a_list)

    eva = int(q_a_list.popleft())

    for a, o in zip(q_a_list, o_list):
        # print(eva, o, a, end=' == ')
        if eva < 0 and o == '//' and int(a) > 0:
            eva = (abs(eva) // int(a)) * -1
        else:
            eva = eval(str(eva) + o + a)
        # print(eva)

    return eva

sol_list = [] 

for i in o_permu:
    sol_list.append(solution(a_list, i))

print(max(sol_list))
print(min(sol_list))