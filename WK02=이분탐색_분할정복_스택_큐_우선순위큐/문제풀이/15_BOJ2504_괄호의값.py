import sys
input = sys.stdin.readline

def parenthesis_count():
    count = 0
    temp = 1
    parenthesis_stack = []
    for index, parenthesis in enumerate(parenthesis_list):
        if parenthesis == '(':
            parenthesis_stack.append(parenthesis_list[index])
            temp *= 2
        elif parenthesis == '[':
            parenthesis_stack.append(parenthesis_list[index])
            temp *= 3
        elif parenthesis == ')':
            if not parenthesis_stack or parenthesis_stack[-1] == '[':
                return 0
            if parenthesis_list[index-1] == '(':
                count += temp
            parenthesis_stack.pop()
            temp //= 2
        else :
            if not parenthesis_stack or parenthesis_stack[-1] == '(':
                return 0
            if parenthesis_list[index-1] == '[':
                count += temp
            parenthesis_stack.pop()
            temp //= 3

    if parenthesis_stack:
        return 0
    return count

parenthesis_list = list(input().rstrip())
print(parenthesis_count())