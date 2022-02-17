import sys

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = dict()

class Trie(object):
    def __init__(self):
        self.head = Node(None)
        self.ans = 0
    
    def insert(self, string):
        cur_node = self.head

        for c in string:
            if c not in cur_node.child:
                cur_node.child[c] = Node(c)
            cur_node = cur_node.child[c]
        
        cur_node.data = string

    def branchCnt(self, cur_node: Node):
        cur_head = cur_node

        if cur_head.data != None and not cur_head.child:
            self.ans += 1
            return

        for child in cur_head.child:            
            self.branchCnt(cur_head.child[child])
            

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    word = [input().rstrip() for _ in range(n)]
    trie = Trie()
    for i in word:
        trie.insert(i)
    trie.branchCnt(trie.head)
    print(trie.ans)




'''
6
hello
hi
h
run
rerun
running

'''

