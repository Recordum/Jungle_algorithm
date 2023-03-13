import sys
input = sys.stdin.readline

n,k = map(int, input().split())

number_list = list(str(input().rstrip()))
number_stack = [number_list[0]]
count = n - k
for i in range(1, len(number_list)):

    while number_stack:
        if len(number_stack) + len(number_list) - i <= n - k:
            break
        if number_stack[-1] < number_list[i]:
            number_stack.pop()
        else:
            break

    if len(number_stack) >= n - k:
        continue

    number_stack.append(number_list[i])


print("".join(number_stack))

