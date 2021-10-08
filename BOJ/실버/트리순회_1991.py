import sys
input = sys.stdin.readline

n = int(input())
tree = dict()
for _ in range(n):
    a, b, c = input().strip().split()
    tree[a] = (b,c)

def pre(node):
    if node != '.':
        print(node, end='')
        pre(tree[node][0])
        pre(tree[node][1])

def inor(node):
    if node != '.':
        inor(tree[node][0])
        print(node, end='')
        inor(tree[node][1])

def post(node):
    if node != '.':
        post(tree[node][0])
        post(tree[node][1])
        print(node, end='')

pre('A')
print()
inor('A')
print()
post('A')