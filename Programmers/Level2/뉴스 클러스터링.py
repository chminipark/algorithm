import math

def solution(str1, str2):
    combine_set = []
    intersection = []

    def make_list(s: str):
        if len(s) == 1:
            return [s]

        str_list = []

        for i in range(len(s)-1):
            if (s[i]+s[i+1]).isalpha():
                str_list.append((s[i]+s[i+1]).lower())
        
        return str_list
    
    str1_list = make_list(str1)
    str2_list = make_list(str2)

    if not str1_list and not str2_list:
        return 65536

    for i in str1_list:
        if i in str2_list:
            intersection.append(i)
            str2_list.remove(i)
    combine_set = str1_list + str2_list

    return math.trunc((len(intersection)/len(combine_set)*65536))


str1 = 'E=M*C^2'
str2 = 'e=m*c^2'
print(solution(str1, str2))