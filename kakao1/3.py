import collections
import math

def solution(fees, records):
    # record 정리
    records_dic = dict()
    for i in records:
        a, b, c = i.split()
        records_dic[int(b)] = list()
    for i in records:
        time,car,inout = i.split()
        records_dic[int(car)].append(time.replace(':',''))

    # 시간 계산
    def cal_time(time_list):
        def minute(less, more):
            less_h, less_m = int(less[:2]), int(less[2:])
            more_h, more_m = int(more[:2]), int(more[2:])
            result_h, result_m = 0,0
            if more_m < less_m:
                more_h -= 1
                result_m = (more_m+60)-less_m
            else:
                result_m = more_m - less_m
            result_h = more_h - less_h
            return (result_h*60)+result_m

        dq = collections.deque(time_list)
        result = 0
        while dq:
            pop = dq.popleft()
            if not dq:
                result += minute(pop, '2359')
            else:
                result += minute(pop, dq.popleft())
        
        return result
    
    # 차 번호순대로
    time_list = []
    for i in sorted(records_dic):
        time_list.append(cal_time(records_dic[i]))

    # 비용계산
    def cost(m):
        nonlocal fees
        if m <= fees[0]:
            return fees[1]
        else:
            return fees[1] + math.ceil((m-fees[0])/fees[2])*fees[3]

    answer = []
    for i in time_list:
        answer.append(cost(i))

    return answer

a = {2:'123', 1:'12', 3:12}
sorted(a)