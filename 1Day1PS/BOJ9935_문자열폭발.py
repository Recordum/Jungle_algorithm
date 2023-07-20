import sys
input = sys.stdin.readline

contents = list(input().rstrip())
bomb = list(input().rstrip())
stack = []

for i in range(len(contents)):
    stack.append(contents[i])
    if len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print("".join(stack))

