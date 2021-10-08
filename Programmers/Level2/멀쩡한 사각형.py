def solution(w,h):
    import math
    b, s, ceil, remove = 0, 0, 0, 0

    if w >= h:
        b = w
        s = h
    else:
        b = h
        s = w
    
    ceil = math.ceil(b/s)
    remove = s * ceil

    return (w*h)-remove

print(solution(8, 12))
