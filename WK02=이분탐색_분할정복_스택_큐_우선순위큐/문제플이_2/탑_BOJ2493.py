import sys
input = sys.stdin.readline

n = int(input())
tower_list = list(map(int, input().split()))
tower_stack = []
result = [0 for _ in range(n)]
for index, tower in enumerate(tower_list):
    if not tower_stack:
        tower_stack.append([tower, index])
        result[index] = 0
        continue

    while tower_stack[-1][0] <= tower :
        tower_stack.pop()
        if not tower_stack:
            break
    if tower_stack:
        result[index] = tower_stack[-1][1] + 1
    else :
        result[index] = 0
    tower_stack.append([tower, index])

for answer in result:
    print(answer)