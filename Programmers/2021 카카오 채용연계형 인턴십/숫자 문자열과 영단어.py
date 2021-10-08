def solution(s):
    answer = ''
    word = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

    def change():
        nonlocal s, answer, word
        for w in word.keys():
            if s.startswith(w,0,5):
                answer += str(word[w])
                s = s[len(w):]
                break
        
    while len(s) != 0:
        try:
            int(s[0])
            answer += s.pop()
        except:
            change()

    return int(answer)


# s = 's123s'
# s[4:]
# try:
#     type(int(s[0]))
# except:
#     print(s[0])

s = "one4seveneight"


print(solution(s))
