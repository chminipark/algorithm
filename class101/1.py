def solution(message, K):
    message = ' ' + message
    if K >= len(message):
        return message.strip()
    elif not message[K].isalpha():
        return message[:K].strip()
    elif not message[K+1].isalpha():
        return message[:K+1].strip()
    else:
        while 0 <= K and message[K].isalpha():
            K -= 1
        return message[:K].strip()
        

