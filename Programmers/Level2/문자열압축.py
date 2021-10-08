import collections

def solution(s):
    compressed_word_list = []

    if len(s) == 1:
        return 1

    def compress(u: int):
        nonlocal s
        queue_s = collections.deque(s)
        compressed_word = ''

        while len(queue_s) >= u*2:
            u_word = ''
            cnt = 1
            for _ in range(u):
                u_word += queue_s.popleft()

            while 1:
                if u_word == ''.join(list(queue_s)[:u]):
                    cnt += 1
                    for _ in range(u):
                        queue_s.popleft()
                else:
                    compressed_word += ('' if cnt == 1 else str(cnt)) + u_word
                    break

        compressed_word += ''.join(queue_s)
        return len(compressed_word)
    
    for i in range(1, len(s)//2+1):
        compressed_word_list.append(compress(i))

    return min(compressed_word_list)

# import collections
# s = "aabbaccc"
# queue_s = collections.deque(s)
# queue_s
# a = ''.join(list(queue_s)[:1])
# a
s = "aabbaccc"
print(solution(s))