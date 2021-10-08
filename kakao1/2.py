import math

def solution(n, k):
    # 진수변환
    def change(n, k):
        reverse = ''

        while n > 0:
            n, m = divmod(n, k)
            reverse += str(m)

        return reverse[::-1] 

    # 소수판별
    def isprime(x):
        if x == 1:
            return False
        for i in range(2, int(math.sqrt(x))+1):
            if x%i == 0:
                return False
        return True

    s = change(n, k)

    answer = 0
    for i in range(1,len(s)+1): 
        for j in range(len(s)):
            if len(s) < j+i:
                continue
            if isprime(int(s[j:j+i])) and '0' not in s[j:j+i]:
                if 0 < j and j+i-1 < len(s)-1:
                    if s[j-1] == '0' and s[j+i] == '0':
                        answer += 1
                elif j == 0 and j+i-1 < len(s) -1:
                    if s[j+i] == '0':
                        answer += 1
                elif j > 0 and j+i-1 == len(s) -1:
                    if s[j-1] == '0':
                        answer += 1
                elif j == 0 and j+i-1 == len(s) -1:
                    answer += 1
    
    return answer
j=0
i=3
s='211020101011'
j == 0 and j+i-1 < len(s) -1

a = '123'
'0' not in a

n = 437674
k = 3

print(solution(n, k))
solution(n, k)
print()

int('437574', 2)
s = str(int(str(n), k))

def change(n, k):
    reverse = ''

    while n > 0:
        n, m = divmod(n, k)
        reverse += str(m)

    return reverse[::-1] 
    
print(solution(45, 3))

