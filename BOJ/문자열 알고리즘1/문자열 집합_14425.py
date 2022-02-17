class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = dict()
    
class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        cur_node = self.head

        for c in string:
            if c not in cur_node.child.keys():
                cur_node.child[c] = Node(c)
            cur_node = cur_node.child[c]
        cur_node.data = string
    
    def find(self, string):
        cur_node = self.head

        for c in string:
            if c not in cur_node.child.keys():
                return False
            cur_node = cur_node.child[c]
        
        if cur_node.data != None and cur_node.data == string:
            return True
        else:
            return False

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trie = Trie()
for _ in range(n):
    trie.insert(input())

ans = 0
for _ in range(m):
    if trie.find(input()):
        ans += 1

print(ans)