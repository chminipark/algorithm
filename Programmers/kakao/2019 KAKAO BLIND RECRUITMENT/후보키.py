from itertools import combinations

def isKey(idx_list, relation):
    check = set()
    for i in range(len(relation)):
        temp = []
        for j in idx_list:
            temp.append(relation[i][j])
        temp = tuple(temp)
        if temp in check:
            return False
        check.add(temp)
    return True

def solution(relation):
    key_list = []
    column_len = len(relation[0])
    column_idx_list = [i for i in range(column_len)]
    for i in range(1, column_len+1):
        for idx_list in combinations(column_idx_list, i):
            idx_set = set(idx_list)
            flag = True
            for k in key_list:
                if k < idx_set:
                    flag = False
                    break
            if flag and isKey(idx_list, relation):
                key_list.append(idx_set)
    
    return len(key_list)


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])