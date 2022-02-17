# delete = []

# def order(cmd, cur, n_key_dic, n_value_dic):
#     global delete
#     if cmd[0] == 'U':
#         jump = int(cmd[2:])
#         c = cur
#         for _ in range(jump):
#             c = n_value_dic[c]
#         return c
#     if cmd[0] == 'D':
#         jump = int(cmd[2:])
#         c = cur
#         for _ in range(jump):
#             c = n_key_dic[c]
#         return c
#     if cmd[0] == 'C':
#         delete.append(cur)
#         if cur == n_value_dic['start']:
#             c, n = cur, n_key_dic[cur]
#             n_value_dic['start'] = n
#             del n_key_dic[c]
#             del n_value_dic[n]
#             return 0
#         elif cur == n_value_dic['end']:
#             prev, c = n_value_dic[cur], cur
#             n_value_dic['end'] = prev
#             del n_key_dic[c]
#             n_key_dic[prev] = 'end'
#             del n_value_dic[c]
#             return prev
#         else:
#             prev, c, n = n_value_dic[cur], cur, n_key_dic[cur]
#             del n_key_dic[c]
#             n_key_dic[prev] = n
#             del n_value_dic[c]
#             n_value_dic[n] = prev
#             return n
#     if cmd[0] == 'Z':
#         item = delete.pop()
#         if item < n_value_dic['start']:
#             n = n_value_dic['start']
#             n_key_dic[item] = n
#             n_value_dic[n] = item
#             n_value_dic['start'] = item
#         elif n_value_dic['end'] < item:
#             prev = n_value_dic['end']
#             n_key_dic[prev] = item
#             n_key_dic[item] = 'end'
#             n_value_dic[item] = prev
#             n_value_dic['end'] = item
#         else:
#             prev, n = 0, 0
#             for k, v in n_key_dic.items():
#                 if k < item < v:
#                     prev, n = k, v
#                     break
#             n_key_dic[item] = n
#             n_key_dic[prev] = item
#             n_value_dic[n] = item
#             n_value_dic[item] = prev
#         return cur




# def solution(n, k, cmd):
#     global delete
#     n_key_dic = dict()
#     n_value_dic = dict()
#     for i in range(n-1):
#         n_key_dic[i] = i+1
#         n_value_dic[i+1] = i
#     n_key_dic[n-1] = 'end'
#     # del n_value_dic[n]
#     n_value_dic['end'] = n-1
#     n_value_dic['start'] = 0

#     for cmdd in cmd:
#         k = order(cmdd, k, n_key_dic, n_value_dic)
    
#     ans = ''
#     for i in range(n):
#         if i in n_key_dic:
#             ans += 'O'
#         else:
#             ans += 'X'
    
#     return ans



# solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])









class Node(object):
    def __init__(self):
        self.prev = None
        self.next = None
        self.removed = False

def solution(n, k, cmd):
    linkedList = [Node() for _ in range(n)]
    for i in range(1, n):
        linkedList[i].prev = linkedList[i-1]
        linkedList[i-1].next = linkedList[i]
    cur_node = linkedList[k]
    deleted = []

    for command in cmd:
        if command[0] == 'U':
            jump = int(command[2:])
            for _ in range(jump):
                cur_node = cur_node.prev
        if command[0] == 'D':
            jump = int(command[2:])
            for _ in range(jump):
                cur_node = cur_node.next
        if command[0] == 'C':
            deleted.append(cur_node)
            cur_node.removed = True
            p_node, n_node = cur_node.prev, cur_node.next
            if p_node:
                p_node.next = n_node
            if n_node:
                n_node.prev = p_node
                cur_node = n_node
            else:
                cur_node = p_node
        if command[0] == 'Z':
            node = deleted.pop()
            node.removed = False
            p_node, n_node = node.prev, node.next
            if p_node:
                p_node.next = node
            if n_node:
                n_node.prev = node

    ans = ''    
    for i in range(n):
        ans += 'O' if not linkedList[i].removed else 'X'
    
    return ans






solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])

