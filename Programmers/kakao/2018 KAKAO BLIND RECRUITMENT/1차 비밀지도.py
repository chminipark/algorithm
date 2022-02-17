def setNum(num, n):
    bin_num = format(num, 'b')
    cnt = n - len(bin_num)
    for _ in range(cnt):
        bin_num = '0' + bin_num
    return bin_num

def solution(n, arr1, arr2):
    ans = []

    for a1, a2 in zip(arr1, arr2):
        a1 = setNum(a1, n)
        a2 = setNum(a2, n)

        wall = ''
        for _a1, _a2 in zip(a1, a2):
            if _a1 == '1' or _a2 == '1':
                wall += '#'
            else:
                wall += ' '
        
        ans.append(wall)
    
    return ans

