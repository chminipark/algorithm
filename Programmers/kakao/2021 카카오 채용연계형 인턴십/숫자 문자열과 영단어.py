class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = dict()

class Trie(object):
    def __init__(self):
        self.head = Node(None)
        self.current = self.head
    
    def insert(self, string):
        cur_node = self.head

        for s in string:
            if s not in cur_node.child:
                cur_node.child[s] = Node(s)
            cur_node = cur_node.child[s]
        
        cur_node.data = string

    def find(self, s):
        self.current = self.current.child[s]
        if self.current.data != None:
            ans = self.current.data
            self.current = self.head
            return ans
        else:
            return 'None'


def solution(s):
    trie = Trie()
    word_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

    for key in word_dic.keys():
        trie.insert(key)
    
    digit_set = {'0','1','2','3','4','5','6','7','8','9'}
    ans = ''
    for i in s:
        if i in digit_set:
            ans += i
            continue
        digit = trie.find(i)
        if digit != 'None':
            ans += word_dic[digit]

    return int(ans)


solution("one4seveneight")