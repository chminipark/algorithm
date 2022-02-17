from itertools import permutations

def cal(op, op_list, num_list):
    to_remove = []
    for i in range(len(op_list)):
        if op_list[i] == op:
            result = eval(num_list[i]+op+num_list[i+1])
            num_list[i+1] = str(result)
            to_remove.append(i)
    for i in range(len(to_remove)):
        del op_list[to_remove[i]-i]
        del num_list[to_remove[i]-i]

def solution(expression):
    num_list = []
    op_list = []

    idx = 0
    n = ''
    while idx < len(expression):
        if expression[idx] == '+' or expression[idx] == '-' or expression[idx] == '*':
            op_list.append(expression[idx])
            num_list.append(n)
            n = ''
            idx += 1
        else:
            n += expression[idx]
            idx += 1
    num_list.append(n)

    op_permu_list = list(permutations(['+', '-', '*'], 3))
    op_set = set(op_list)

    ans = 0
    for possible_list in op_permu_list:
        tmp_op_list = op_list[:]
        tmp_num_list = num_list[:]
        for oper in possible_list:
            if oper in op_set:
                cal(oper, tmp_op_list, tmp_num_list)
        ans = max(ans, abs(int(tmp_num_list[0])))
    
    return ans
            



solution("100-200*300-500+20")