def solution():
    prime_list = [True] * (10**(n))
    prime_list[0] = False
    prime_list[1] = False
    ans = []

    def isAmazingPrime(s):
        s = str(s)
        flag = True
        for i in range(len(s)):
            if not prime_list[int(s[:i+1])]:
                flag = False
        return flag

    for i in range(2, len(prime_list)):
        if prime_list[i]:
            for j in range(i*2, len(prime_list), i):
                prime_list[j] = False
            if i >= 10**(n-1):
                if isAmazingPrime(i):
                    ans.append(i)
    print(*ans, sep='\n')

if __name__ == '__main__':
    n = int(input())
    solution()