import sys
input = sys.stdin.readline

n = int(input())

tower_list = list(map(int, input().split()))
receive_index = [0 for i in range(n)]
tower_stack = []
for i in range(len(tower_list)):
    while tower_stack:
        if tower_stack[-1][0] > tower_list[i]:
            receive_index[i] = tower_stack[-1][1]
            break

        if tower_stack[-1][0] <= tower_list[i]:
            tower_stack.pop()

    tower_stack.append([tower_list[i],i + 1])

print(" ".join(map(str, receive_index)))

