import sys
input = sys.stdin.readline

# 10
# 10 -4 3 1 5 6 -35 12 21 -1

n = int(input())
number_list = list(map(int, input().split()))
result_stack = []
delete_stack = []
for i in range(len(number_list)):
    if i == len(number_list)-1 and number_list[i] < 0:
        break
    if number_list[i] < 0:
        if not delete_stack:
            delete_stack.append(number_list[i])
        elif delete_stack[0] > number_list[i]:
            result_stack.append(delete_stack.pop())
            delete_stack.append(number_list[i])
        elif delete_stack[0] <= number_list[i]:
            result_stack.append(number_list[i])
    else:
        result_stack.append(number_list[i])

print(sum(result_stack))
            