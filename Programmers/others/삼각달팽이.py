# def solution(n):
#     answer = []

#     for i in range(1,n+1):
#         answer.append([0]*i)

#     def drawing(top_idx, top_num, move):
#         # top_idx 0,2,4,6
#         # cnt 0,1,2,3
#         # move n-1, 5
#         if move <= 0:
#             if move == 0:
#                 answer[top_idx][top_idx//2] == top_num
#                 return
#             else :
#                 return
        
#         for i in range(move):
#             answer[top_idx+i][top_idx//2] = top_num
#             top_num += 1
#         for i in range(move):
#             answer[top_idx+move][top_idx//2+i] = top_num
#             top_num += 1
#         for i in range(move):
#             answer[top_idx+move-i][-(top_idx//2)-1] = top_num
#             top_num += 1
        
#         drawing(top_idx+2, top_num, move-3)

#     drawing(0, 1, n-1)

#     for i in answer:
#         print(i)

# solution(5)


def solution(n):
    answer = []

    for i in range(1,n+1):
        answer.append([0]*i)

    def drawing(top_idx, top_num, move):
        # top_idx 0,2,4,6
        # cnt 0,1,2,3
        # move n-1, 5
        if move <= 0:
            if move == 0:
                answer[top_idx][top_idx//2] = top_num
                return
            else :
                return
        
        for i in range(move):
            answer[top_idx+i][top_idx//2] = top_num
            top_num += 1
        for i in range(move):
            answer[top_idx+move][top_idx//2+i] = top_num
            top_num += 1
        for i in range(move):
            answer[top_idx+move-i][-(top_idx//2)-1] = top_num
            top_num += 1
        
        drawing(top_idx+2, top_num, move-3)

    drawing(0, 1, n-1)
    answer = sum(answer, [])
    return answer
    
solution(4)