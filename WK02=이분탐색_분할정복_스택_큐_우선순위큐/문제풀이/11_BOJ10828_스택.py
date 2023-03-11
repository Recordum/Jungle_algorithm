import sys
input = sys.stdin.readline

def run_instruction():
    if instruction[0] == 'push':
        stack.append(instruction[1])
        return

    if instruction[0] == 'pop':
        if len(stack) > 0:
            result.append(stack.pop())
            return
        result.append(-1)
        return

    if instruction[0] == 'size':
        result.append(len(stack))
        return

    if instruction[0] == 'empty':
        if len(stack) > 0:
            result.append(0)
            return
        result.append(1)
        return

    if instruction[0] == 'top':
        if len(stack) > 0:
            result.append(stack[-1])
            return
        result.append(-1)
        return



n = int(input())
result= []
stack = []
for _ in range(n):
    instruction = list(map(str, input().split()))
    run_instruction()

for answer in result:
    print(answer)