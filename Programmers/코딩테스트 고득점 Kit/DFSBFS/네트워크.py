def solution(n, computers):

    def find_parent(a):
        if parent[a] == a:
            return a
        p = find_parent(parent[a])
        parent[a] = p
        return p
    
    def union(a, b):
        a = find_parent(a)
        b = find_parent(b)

        if a == b:
            return
        
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1:
                union(i,j)
    
    ans = set()
    for i in range(n):
        ans.add(find_parent(i))
    return len(ans)




    

'''
[[1, 1, 0], [1, 1, 0], [0, 0, 1]]

'''

