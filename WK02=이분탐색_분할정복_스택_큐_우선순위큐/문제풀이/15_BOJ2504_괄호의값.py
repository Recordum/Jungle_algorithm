import sys
input = sys.stdin.readline


def recursive_parenthesis(temp,temp_count):
    global count
    for i in range(len(parenthesis_list)):
        if not visited[i]:
            if parenthesis_list[i] == '(':
                visited[i] = True
                parenthesis_stack.append(parenthesis_list[i])
                temp_count = recursive_parenthesis(temp,temp_count)
                if not '(' in parenthesis_stack:
                    count = temp_count + count
                continue
            if parenthesis_list[i] == '[':
                visited[i] = True
                parenthesis_stack.append(parenthesis_list[i])
                temp_count = recursive_parenthesis(temp, temp_count)
                if not '[' in parenthesis_stack:
                    count = temp_count + count
                continue
            if parenthesis_list[i] == ')':
                visited[i] = True
                if not '(' in parenthesis_stack or parenthesis_stack[-1] == '[':
                    print(0)
                    exit()
                parenthesis_stack.pop()
                temp = temp * 2
                return temp
            if parenthesis_list[i] == ']':
                visited[i] = True
                if not '[' in parenthesis_stack or parenthesis_stack[-1] == '(':
                    print(0)
                    exit()
                parenthesis_stack.pop()
                temp = temp * 3
                return temp

    return
parenthesis_list = list(input().rstrip())
count = 0
visited = [False for _ in range(len(parenthesis_list))]
parenthesis_stack = []
number = 0
temp = 1

print(recursive_parenthesis(1,0))


