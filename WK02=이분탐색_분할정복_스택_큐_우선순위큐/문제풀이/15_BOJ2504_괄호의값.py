import sys
input = sys.stdin.readline


def recursive_parenthesis():
    temp = 1
    for i in range(len(parenthesis_list)-1):
        if parenthesis_list[i] == '(':
            parenthesis_stack.append('(')
            temp *= 2
        if parenthesis_list[i] == '[':
            parenthesis_stack.append('[')
            temp *= 3
        if parenthesis_list[i] == ')':
            if not '(' in parenthesis_stack:
                print(0)
                exit()
            parenthesis_stack.remove('(')
            if not '(' in parenthesis_stack:
                value = 0
                for stack in parenthesis_stack:
                    if type(stack) == int:
                        value += stack
                        parenthesis_stack.remove(stack)
                parenthesis_stack.append(value * temp)

        if parenthesis_list[i] == ']':
            temp = 3
            if not '[' in parenthesis_stack:
                print(0)
                exit()
            parenthesis_stack.remove('[')
            parenthesis_stack.append(temp)
            if not '[' in parenthesis_stack:
                value = 0
                for stack in parenthesis_stack:
                    if type(stack) == int:
                        value += stack
                        parenthesis_stack.remove(stack)
                parenthesis_stack.append(value * temp)
    return


parenthesis_list = list(input().rstrip())
visited = [False for _ in range(len(parenthesis_list))]
parenthesis_stack = []
number = 0
temp = 1
recursive_parenthesis(0)
print(parenthesis_stack)


