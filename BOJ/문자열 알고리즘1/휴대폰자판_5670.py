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
    
    def inputCount(self, string):
        cur_node = self.head.child[string[0]]
        cnt = 1
        cur_word = string[0]
        if cur_word == string:
            return cnt
        for i in range(1, len(string)):
            cur_keys_count = len(cur_node.child.keys())
            cur_node = cur_node.child[string[i]]
            if cur_keys_count >= 2 or cur_node.data != None:
                cnt += 1
            if cur_word == cur_node.data:
                break
        return (cnt-1 if cnt > 1 else cnt)

import sys

input = sys.stdin.readline

answer = []
try:
    while True:
        n = int(input())
        w_list = []
        trie = Trie()
        for _ in range(n):
            word = input().strip()
            w_list.append(word)
            trie.insert(word)
        ans = []
        for i in w_list:
            ans.append(trie.inputCount(i))
        answer.append(sum(ans)/len(ans))

except:
    print(*answer, sep='\n')
    sys.exit()