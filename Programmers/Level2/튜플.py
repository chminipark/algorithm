import collections

def solution(s):
    counter = []

    cnt = 0
    for i in range(len(s)):
        if s[i].isdigit():
            cnt += 1
        elif cnt > 0:
            counter.append(int(s[i-cnt:i]))
            cnt = 0

    sorted_couter = collections.Counter(counter).most_common()
    answer = [x for x, y in sorted_couter]

    return answer


counter = []

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

cnt = 0
for i in range(len(s)):
    if s[i].isdigit():
        cnt += 1
    elif cnt > 0:
        counter.append(int(s[i-cnt:i]))
        cnt = 0

counter




answer