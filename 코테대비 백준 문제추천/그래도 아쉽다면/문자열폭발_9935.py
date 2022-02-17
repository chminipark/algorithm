import sys

def solution():
    stack = []
    for i in word:
        stack.append(i)
        while len(stack) >= len(ex_word_list) and stack[-len(ex_word_list):] == ex_word_list:
            for _ in range(len(ex_word_list)):
                stack.pop()
    
    if stack:
        print(''.join(stack))
    else:
        print('FRULA')


if __name__ == '__main__':
    input = sys.stdin.readline
    word = input().rstrip()
    ex_word_list = list(input().rstrip())

    solution()