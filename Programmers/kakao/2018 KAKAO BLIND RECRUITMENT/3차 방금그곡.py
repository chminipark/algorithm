def cal_time(a, b):
    a_h, a_m, b_h, b_m = int(a[:2]), int(a[3:]), int(b[:2]), int(b[3:])
    h, m = b_h - a_h, b_m - a_m
    if m < 0:
        m += 60
        h -= 1
    if h < 0:
        h = 0
    return (h * 60) + m

def cal_scale(scale, minute):
    result = ''
    sharp_cnt = scale.count('#')
    multi = minute // (len(scale) - sharp_cnt)
    rest = minute % (len(scale) - sharp_cnt)
    result = multi * scale

    idx = 0
    rest_cnt = 0
    while rest_cnt < rest:
        result += scale[idx]
        if idx != len(scale)-1 and scale[idx+1] == '#':
            result += scale[idx+1]
            idx += 1
        idx += 1
        rest_cnt += 1

    return result

def solution(m, musicinfos):
    # [재생시간, 코드, 이름]
    music_list = []
    # [재생시간, idx]
    ans = []

    for i in musicinfos:
        a,b,c,d = i.split(',')
        play_time = cal_time(a, b)
        full_scale = cal_scale(d, play_time)
        music_list.append([play_time, full_scale, c])
    
    for i in range(len(music_list)):
        play_time, full_scale, name = music_list[i]
        idx = 0
        flag = False
        while idx + len(m) <= len(full_scale):
            if m == full_scale[idx:idx+len(m)]:
                flag = True
            if idx+len(m) < len(full_scale) and full_scale[idx+len(m)] == '#':
                flag = False
            if flag: break
            idx += 1

        if flag:
            ans.append([play_time, i])
    
    ans.sort(key=lambda x: (-x[0], x[1]))


    # print(music_list[ans[0][1]][2] if ans else '(None)')
    # print(ans)
    # print(music_list)

    return music_list[ans[0][1]][2] if ans else '(None)'


solution("CC#BCC#BCC#", ["03:00,03:08,FOO,CC#B"])




# solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# solution("CC#BCC#BCC#BCC#B"	, ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
# solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])