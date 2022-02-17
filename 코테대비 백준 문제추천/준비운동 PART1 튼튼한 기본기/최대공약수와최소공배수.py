a, b = map(int, input().split())

high = max(a, b)
low = min(a, b)

def gcd(h, l):
    while l:
        h, l = l, h%l
    return h

gcdd = gcd(high, low) 
print(gcdd)
print((a*b)//gcdd)