import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().rstrip()))
number_stack = []

for i in range(n):
    if not number_stack:
        number_stack.append(number[i])
        continue
    if n - len(number_stack) == n-i+1:
        number_stack.pop()
        number_stack.append(number[i])
        continue
    if n - len(number_stack) <= n-i+1:
        number_stack.append(number[i])
        continue
    if number_stack[-1] <= number[i]:
        if number_stack[-1] != number[i]:
            number_stack.pop()
        number_stack.append(number[i])
        continue

print(number_stack)