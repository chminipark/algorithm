import sys
sys.setrecursionlimit(10**9)

class Tree(object):
    def __init__(self, dataList):
        self.data = max(dataList, key=lambda x: x[1])
        self.left = None
        self.right = None

        leftList = list(filter(lambda x: x[0] < self.data[0], dataList))
        rightList = list(filter(lambda x: x[0] > self.data[0], dataList))

        if leftList: self.left = Tree(leftList)
        if rightList: self.right = Tree(rightList)
    
def prepost(node, pre, post):
    pre.append(node.data)
    if node.left != None:
        prepost(node.left, pre, post)
    
    if node.right != None:
        prepost(node.right, pre, post)
    post.append(node.data)


def solution(nodeinfo):
    tree = Tree(nodeinfo)
    preorder = []
    postorder = []
    prepost(tree, preorder, postorder)

    ans = []
    ans.append(list(map(lambda x: nodeinfo.index(x)+1, preorder)))
    ans.append(list(map(lambda x: nodeinfo.index(x)+1, postorder)))
    return ans










solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])


'''
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

'''