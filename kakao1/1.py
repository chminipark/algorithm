import collections

def solution(id_list, report, k):

    mail_dic = dict()
    for i in id_list:
        mail_dic[i] = set()
    report_temp = []
    report_k = []

    for i in report:
        user_id, user_reported_id = i.split()
        mail_dic[user_id].add(user_reported_id)

    for i in mail_dic.values():
        report_temp += list(i)

    for x, y in collections.Counter(report_temp).most_common():
        if y >= k:
            report_k.append(x)
        else:
            break
    
    answer = []
    report_k = set(report_k)
    for i in id_list:
        answer.append(len(mail_dic[i] & report_k))
    
    return answer

a = [1, 2, 3, 3]
b = [1,2]
a+b
collections.Counter(a).most_common()

a = '123 2424'
a = dict()
a['1'] = {1,2,3}
a['2'] = {2,3,4}
for i in a.values():
    print(i)
a['1'].append(2)
a['1']