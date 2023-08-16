import sys
input = sys.stdin.readline

def find_password(key_log):
    left_stack = []
    right_stack = []

    for key in key_log:
        if key == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
            continue
        if key == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
            continue
        if key == '-':
            if left_stack:
                left_stack.pop()
            continue
        left_stack.append(key)

    return left_stack + list(reversed(right_stack))

n = int(input())
key_log_list = [list(map(str, input().rstrip())) for _ in range(n)]
result = []
for key_log in key_log_list:
    result.append(find_password(key_log))

for ans in result:
    print("".join(ans))

