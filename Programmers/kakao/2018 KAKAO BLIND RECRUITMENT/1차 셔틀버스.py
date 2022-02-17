def nextBusTime(cur_time, interval):
    h, m = cur_time[0], cur_time[1]
    m += interval
    if m >= 60:
        m = m - 60
        h += 1
    return [h, m]

def minusOneTime(cur_time):
    h, m = cur_time[0], cur_time[1]
    m -= 1
    if m == -1:
        h -= 1
        m = 59
    return [h, m]

def isInTime(crew_time, depart_time):
    if crew_time[0] < depart_time[0]:
        return True
    if crew_time[0] == depart_time[0]:
        if crew_time[1] <= depart_time[1]:
            return True
    return False

def makeTime(time):
    h, m = str(time[0]), str(time[1])
    h = '0' + h if len(h) == 1 else h
    m = '0' + m if len(m) == 1 else m
    return h + ':' + m

def solution(n, t, m, timetable):
    crew = []
    for i in timetable:
        a, b = int(i[:2]), int(i[3:])
        crew.append([a, b])
    crew.sort(reverse=True)

    depart_time = [9,0]
    bus = 0
    ans = [0,0]

    for _ in range(n):
        if depart_time[0] >= 24:
            break

        while bus < m:
            if crew and isInTime(crew[-1], depart_time):
                ans = crew.pop()               
                bus += 1
            else:
                break
        
        if bus == m:
            ans = minusOneTime(ans)
        else:
            ans = depart_time

        bus = 0
        depart_time = nextBusTime(depart_time, t)
    
    return makeTime(ans)



solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])
solution(2,10,2,["09:10", "09:09", "08:00"])


'''
timetable -> 이차원배열, 정렬


출발시간 체크 



'''