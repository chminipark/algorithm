from collections import deque

def Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = dict()

def Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        cur_node = self.head
        for s in string:
            if s not in cur_node.child:
                cur_node.child[s] = Node(s)
            cur_node = cur_node.child[s]
        cur_node.data = string
    
    def isWordInTrie(self, word):
        cur_node = self.head
        for s in word:
            if s not in cur_node.child:
                return None
            cur_node = cur_node[s]
        return cur_node
    
    def calCnt(self, cnt, node):
        q = deque()
        # (node, depth)
        q.append((node, 0))

        ans = 0
        while q:
            cur_node, depth = q.popleft()

            if cur_node.data != None and depth == cnt:
                ans += 1
                continue

            if depth == cnt:
                continue

            for nex_node in cur_node.child.values():
                q.append(nex_node, depth+1)
        
        return ans



def solution(words, queries):
    trie = Trie()
    reversedTrie = Trie()

    for w in words:
        trie.insert(w)
        reversedTrie.insert(reversed(w))
    





'''

["frodo", "front", "frost", "frozen", "frame", "kakao"]
["fro??", "????o", "fr???", "fro???", "pro?"]
[3, 2, 4, 1, 0]

'''


