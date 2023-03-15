import sys
input = sys.stdin.readline

element = 1
n = int(input())
stack = []
result = []
compare = []
goal_list = [int(input()) for _ in range(n)]
for index, goal in enumerate(goal_list):
    while element <= goal:
        stack.append(element)
        element += 1
        result.append('+')

    while stack:
        if stack[-1] == goal:
            compare.append(stack.pop())
            result.append('-')
        else :
            break
if compare != goal_list:
    print('NO')
else:
    for answer in result:
        print(answer)
