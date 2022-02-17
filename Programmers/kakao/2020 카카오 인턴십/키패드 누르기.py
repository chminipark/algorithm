def distance(hand_cordi, num_cordi):
    return abs(hand_cordi[0]-num_cordi[0]) + abs(hand_cordi[1]-num_cordi[1])

def solution(numbers, hand):
    keypad = dict()

    n = 1
    for i in range(3):
        for j in range(3):
            keypad[n] = (i,j)
            n += 1
    keypad[0] = (3,1)

    current = [(3,0), (3,2)]
    leftNum = {1,4,7}
    rightNum = {3,6,9}

    ans = ''
    for num in numbers:
        if num in leftNum:
            current[0] = keypad[num]
            ans += 'L'
        elif num in rightNum:
            current[1] = keypad[num]
            ans += 'R'
        else:
            leftdist = distance(current[0], keypad[num])
            rightdist = distance(current[1], keypad[num])

            if leftdist == rightdist:
                if hand == 'left':
                    current[0] = keypad[num]
                    ans += 'L'
                else:
                    current[1] = keypad[num]
                    ans += 'R'
            elif leftdist < rightdist:
                current[0] = keypad[num]
                ans += 'L'
            else:
                current[1] = keypad[num]
                ans += 'R'
    
    return ans








solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")

'''

[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"



'''