def solution(s):
    from collections import Counter

    tmp = []
    idx = 0
    num = ''
    while idx < len(s):
        if s[idx] == '{' or s[idx] == '}' or s[idx] == ',':
            idx += 1
            if num:
                tmp.append(int(num))
                num = ''
        else:
            num += s[idx]
            idx += 1
    
    count = Counter(tmp)
    answer = [0] * (len(count))
    for value, index in count.items():
        answer[len(count) - index] = int(value)
    
    return answer

# solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{20,111},{111}}")
