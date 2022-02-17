def solution(gems):
    from collections import Counter
    gems_set = set(gems)

    start, end = 0, len(gems_set)-1
    gems_dic = Counter(gems[start:end+1])
    ans = [0, len(gems)]

    while True:
        if len(gems_dic) != len(gems_set):
            end += 1
            gems_dic[gems[end]] += 1
        else:
            if ans[1]-ans[0] > end-start:
                ans = [start+1, end+1]
            if gems_dic[gems[start]] == 1 or (end+1) - start <= len(gems_set):
                end += 1
                if end == len(gems):
                    break
                gems_dic[gems[end]] += 1
            else:
                gems_dic[gems[start]] -= 1
                start += 1
                
    return ans


    print(ans)

        

        




    
    # return [ans[0]+1,ans[1]+1]



solution(["a", "b", "c", "b", "c", "d", "f", "d", "b", "e", "g", "e", "a"])
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])


# a = {'1':1, '2':2, '3':3}
# a.keys()


# {'1','2'} in {'1','2','3'}



'''
["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
[3, 7]




'''