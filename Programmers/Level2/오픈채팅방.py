def solution(record):
    answer = []
    uid_nickname_dic = {}

    for i in record:
        i_list = i.split()
        if i_list[0] == 'Enter' or i_list[0] == 'Change':
            uid_nickname_dic[i_list[1]] = i_list[2]
    
    for i in record:
        i_list = i.split()
        if i_list[0] == 'Enter':
            nickname = uid_nickname_dic[i_list[1]]
            message = f"{nickname}님이 들어왔습니다."
            answer.append(message)
        elif i_list[0] == 'Leave':
            nickname = uid_nickname_dic[i_list[1]]
            message = f"{nickname}님이 나갔습니다."
            answer.append(message)

    return answer

# a = "Enter uid1234 Muzi"
# a_list = a.split()
# print(type(a_list))
# b = 'uid1234' in a
# print(b)

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

result = solution(record)
print(result)