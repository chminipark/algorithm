import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

index = [0]*(n+1)
for i,x in enumerate(inorder):
    index[x] = i

def preorder(in_start, in_end, post_start, post_end):

    if (in_start > in_end) or (post_start > post_end):
        return

    parent = postorder[post_end]
    print(parent, end=' ')

    left = index[parent] - in_start
    right = in_end - index[parent]
    
    #left
    preorder(in_start, left, post_start, post_end)
    #right


