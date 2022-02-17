import sys
sys.setrecursionlimit(10**9)

def find_parent(x, visited):
    if x not in visited:
        visited[x] = x+1
        return x
    p = find_parent(visited[x], visited)
    visited[x] = p
    return p

def solution(k, room_number):
    visited = dict()
    ans = []

    for i in room_number:
        num = find_parent(i, visited)
        ans.append(num)
    
    return ans

solution(10, [1,3,4,1,3,1])