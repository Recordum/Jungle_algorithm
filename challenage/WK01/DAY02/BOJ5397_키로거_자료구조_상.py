import sys
input = sys.stdin.readline

# 오답/ 실버2
# 접근은 맞았으나, 오른쪽 스택을 reverse에서 합쳐야하는것을 빼먹어서 30분초과
# 실제 시간을 재면서 하면 엣지케이스를 충분히 검토하지 못하는상황
# 아이디어를 좀더 빨리 떠올리거나, 여러케이스를 빠르게 시도해야할듯
# 혹은 stack 이아닌 dequeue로 풀면 뒤집는 부분을 생각하지 않아도되서 직관적일듯 
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
result = []
test_case = [list(map(str, input().rstrip())) for _ in range(n)]

for key_log in test_case:
    password = find_password(key_log)
    result.append(password)
for ans in result:
    print("".join(ans))