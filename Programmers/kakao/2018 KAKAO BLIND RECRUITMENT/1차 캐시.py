from collections import deque

def solution(cacheSize, cities):
    buffer = deque()

    if cacheSize == 0:
        return len(cities) * 5

    ans = 0
    for city in cities:
        city = city.lower()
        if city in buffer:
            ans += 1
        else:
            ans += 5
        
        if city in buffer:
            buffer.remove(city)
        elif len(buffer) == cacheSize:
            buffer.popleft()
        
        buffer.append(city)
    
    return ans
