def binSearch(target, data):
    data.sort()
    start, end = 0, len(data)-1

    while start <= end:
        mid = (start+end) // 2

        if data[mid] == target:
            return mid
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return start

a = [4,5,6,3,7,2,1,102,324,22]

print(binSearch(4, a))
