def solution(msg):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    word_dic = dict()
    for i in range(1, len(alphabet)+1):
        word_dic[alphabet[i-1]] = i

    idx = len(word_dic)+1
    start, end = 0, 1
    ans = []
    while start < len(msg):
        while end <= len(msg):
            if msg[start:end] in word_dic:
                end += 1
            else:
                break
        ans.append(word_dic[msg[start:end-1]])
        word_dic[msg[start:end]] = idx
        idx += 1

        start = end - 1
        end = start + 1

    return ans

solution('KAKAO')
solution('TOBEORNOTTOBEORTOBEORNOT')
solution('ABABABABABABABAB')