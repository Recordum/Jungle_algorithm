import sys

def dfs(previous_result, next_number, operation_list, depth):
    global min_answer
    global max_answer

    if operation_list[0] == operation_list[1] == operation_list[2] == operation_list[3] == 0:
        if min_answer > previous_result:
            min_answer = previous_result
        if max_answer < previous_result:
            max_answer = previous_result
        return

    for i in range(4):
        if operation_list[i] > 0:
            if i == 0:
                current_result = previous_result + a[next_number]
            elif i == 1:
                current_result = previous_result - a[next_number]
            elif i == 2:
                current_result = previous_result * a[next_number]
            elif i == 3:
                if previous_result < 0:
                    current_result = -((-previous_result) // a[next_number])
                else:
                    current_result = previous_result // a[next_number]

            operation_list[i] -= 1
            dfs(current_result, next_number + 1, operation_list, depth + 1)
            operation_list[i] += 1


input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
operation_list = list(map(int, input().split()))
max_answer = -1e9
min_answer = 1e9

dfs(a[0], 1, operation_list, 0)

print(max_answer)
print(min_answer)