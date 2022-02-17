class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.child = dict()
        self.data = data

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        cur_node = self.head
        for s in string:
            if s not in cur_node.child:
                cur_node.child[s] = Node(s)
            cur_node = cur_node.child[s]
        cur_node.data = string
    
    def inputNum(self, string):
        cur_node = self.head
        depth = 0
        ans = 1
        for i in range(len(string)):
            cur_node = cur_node.child[string[i]]
            depth += 1
            if len(cur_node.child) >= 2:
                ans = depth + 1
            if i != len(string) - 1 and cur_node.data != None:
                ans = depth + 1

        if cur_node.child:
            ans = len(string)
        
        return ans

def solution(words):
    trie = Trie()

    for w in words:
        trie.insert(w)
    
    ans = 0
    for w in words:
        ans += trie.inputNum(w)
    
    return ans

solution(["go","gone","guild"])
solution(["abc","def","ghi","jklm"])
solution(["word","war","warrior","world"])




# a = {1: '1', 2: '2'}
# len(a)