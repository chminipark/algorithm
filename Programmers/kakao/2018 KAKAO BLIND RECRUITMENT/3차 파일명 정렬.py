def separateWord(word):
    start = 0
    head, number, tail = '', '', ''

    # head
    for i in range(len(word)):
        if word[i].isdigit():
            head = word[:i]
            start = i
            break
    
    # number
    for i in range(start, len(word)):
        if not word[i].isdigit():
            number = word[start:i]
            start = i
            break
    else:
        number = word[start:]
        start = len(word)
    
    tail = word[start:]
    return [head, number, tail]

    
def solution(files):
    files_list = []
    for word in files:
        files_list.append(separateWord(word))

    files_list.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return list(map(lambda x: ''.join(x), files_list))

# solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
# solution(["muzi1.png1", "MUZI1.png2", "MUZI1.png3", "muzi1.png4"])
solution(['ABC12','AbC12','aBc12'])






'''
1. head 비교
2. number 비교
3. 먼저 입력된 idx 순.. 
'''


'''
입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

'''