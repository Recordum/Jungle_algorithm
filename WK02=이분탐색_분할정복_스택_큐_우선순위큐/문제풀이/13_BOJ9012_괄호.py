import sys
input = sys.stdin.readline

n = int(input())
result = ['' for _ in range(n)]
for i in range(n):
    parenthesis_string = input().strip()
    result[i] = 'YES'
    parenthesis_stack = []
    for parenthesis in parenthesis_string:
        if parenthesis == ')':
            if '(' in parenthesis_stack:
                parenthesis_stack.remove('(')
                continue
            else :
                result[i] = 'NO'
                break

        parenthesis_stack.append(parenthesis)

    if parenthesis_stack:
        result[i] = 'NO'
for answer in result:
    print(answer)