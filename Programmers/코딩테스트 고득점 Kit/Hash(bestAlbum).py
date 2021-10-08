def solution(genres, plays):

    genresDic = {}

    for i in range(len(genres)):
        if genres[i] in genresDic:
            genresDic[genres[i]] = genresDic[genres[i]] + plays[i]
        else:
            genresDic[genres[i]] = plays[i]

    sortedGenres = sorted(genresDic, key = lambda x : genresDic[x], reverse= True)
    print(sortedGenres)

    
    for i in sortedGenres:
        for j in range(len(genres)):
            if i == genres[j]:
                if plays[j] > mostplayed:
                    mostplayed = plays[j]
                    mostplayedindex = j
        del 



    answer = []
    return answer

a = ["classic", "pop", "classic", "classic", "pop"]
b = [500, 600, 150, 800, 2500]

sol = solution(a, b)
