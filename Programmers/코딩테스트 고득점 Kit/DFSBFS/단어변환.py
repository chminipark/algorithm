def solution(begin, target, words):
    if target not in words:
        return 0
    
    stack = []
    stack.append(begin)

    ans = 0
    while stack:
        cur = stack.pop()

        for word in words:
            cnt = 0
            for i in range(len(word)):
                if word[i] != cur[i]:
                    cnt += 1
            if cnt == 1 and word == target:
                return ans + 1
            if cnt == 1:
                stack.append(word)
        
        ans += 1
    
    return ans


                

            
    




'''

"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4

stack, dfs
depth -> +1

'''