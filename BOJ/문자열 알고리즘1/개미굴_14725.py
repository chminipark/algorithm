class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        cur_node = self.head

        for c in string:
            if c not in cur_node.child:
                cur_node.child[c] = Node(c)
            cur_node = cur_node.child[c]
        cur_node.data = string
    
    def print_trie(self, l, cur_node: Node):
        if cur_node.data != None:
            return
        
        sorted_child = sorted(cur_node.child)

        for ch in sorted_child:
            print('--'*l + ch)
            self.print_trie(l+1, cur_node.child[ch])


import sys

input = sys.stdin.readline

n = int(input())
trie = Trie()
for _ in range(n):
    tmp = input().strip().split(' ')
    trie.insert(tmp[1:])

trie.print_trie(0, trie.head)



        
