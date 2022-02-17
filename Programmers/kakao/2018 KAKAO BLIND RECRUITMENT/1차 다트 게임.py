def SDT(score, bonus):
    if bonus == 'S':
        return int(score)
    if bonus == 'D':
        return int(score) ** 2
    if bonus == 'T':
        return int(score) ** 3

def Query_separ(query):
    a, b, c = '', '', ''
    if query[0].isdecimal() and query[1].isdecimal():
        a = query[:2]
        b = query[2]
        c = 'N'
        if len(query) == 4:
            c = query[3]
    else:
        a, b, c = query[0], query[1], 'N'
        if len(query) == 3:
            c = query[2]
    
    return (a, b, c)

def Dart_separ(dart):
    q_list = []
    s = 0
    for i in range(1, len(dart)):
        if dart[i-1].isdecimal():
            continue
        if len(q_list) == 2:
            break
        if dart[i].isdecimal():
            q_list.append(dart[s:i])
            s = i
    q_list.append(dart[s:])
    
    return q_list

def solution(dartResult):
    score = []
    start = 0
    query_list = Dart_separ(dartResult)

    for q in query_list:
        a, b, c = Query_separ(q)

        score.append(SDT(a, b))

        if c != 'N':
            if c == '*':
                score[-1] = score[-1] * 2
                if len(score) >= 2:
                    score[-2] = score[-2] * 2
            elif c == '#':
                score[-1] = score[-1] * (-1)
    
    return sum(score)

solution('1D2S#10S')

            