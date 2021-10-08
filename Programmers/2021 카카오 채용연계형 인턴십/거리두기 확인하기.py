def solution(s):
    answer = 1
    index = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    while s:
        for i in range(len(s)-1):
            index = i
            if s[i] == s[i+1]:
                s = s.replace(s[i],'')
                break
        if index == len(s)-1:
            answer = -1
            break

    return answer

print(solution('baabaa'))