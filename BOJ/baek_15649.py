# import sys
# import itertools

# inputsys = sys.stdin.readline().rstrip('\n')

# N, M = map(int, inputsys.split())
# A = ''.join(map(str, list(range(1, N+1))))
# for i in itertools.permutations(A, M):
#     print(' '.join(i))


# import sys 

# N, M = list(map(int, sys.stdin.readline().split()))

# S = []

# def dfs():
#     if len(S) == M:
#         print(' '.join(map(str, S)))
#         return

#     for i in range(1, N+1):
#         if i not in S:
#             S.append(i)
#             dfs()
#             S.pop()
