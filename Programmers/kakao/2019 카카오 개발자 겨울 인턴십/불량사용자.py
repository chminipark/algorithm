from itertools import permutations

def isPossible(userId, bannedId):
    for i in range(len(userId)):
        if len(userId[i]) != len(bannedId[i]):
            return False
        for a, b in zip(userId[i], bannedId[i]):
            if b == '*':
                continue
            if a != b:
                return False
    return True

def solution(user_id, banned_id):
    possible_list = list(permutations(user_id, len(banned_id)))

    banned_set = []
    for user_list in possible_list:
        if isPossible(user_list, banned_id):
            user_list_set = set(user_list)
            if user_list_set not in banned_set:
                banned_set.append(user_list_set)
    
    return len(banned_set)






solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
                    


'''




'''