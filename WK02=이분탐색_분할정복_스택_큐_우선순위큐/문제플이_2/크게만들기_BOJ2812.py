import sys
input = sys.stdin.readline

n, k = map(int,input().split())
number_list = input().rstrip()
number_stack = []

for index, number in enumerate(number_list):
    if not number_stack:
        number_stack.append(number)
        continue

    if len(number_stack) <= index + k:
        number_stack.append(number)
        continue

    if number_stack[-1] < number:
        number_stack.pop()
        number_stack.append(number)

print(number_stack)