import sys
input = sys.stdin.readline

def dfs(depth, value, current_index, current_oper):
    global max_result
    global min_result
    if depth > 1:
        if current_oper == 0:
            value = value + numbers_list[current_index]
        elif current_oper == 1:
            value = value - numbers_list[current_index]
        elif current_oper == 2:
            value = value * numbers_list[current_index]
        else:
            value = int(value / numbers_list[current_index])

    if depth == n:
        max_result = max(max_result, value)
        min_result = min(min_result, value)
        return


    for i in range(current_index + 1,n):
        for j in range(4):
            if  oper[j] != 0:
                oper[j] -= 1
                dfs(depth+1 , value, i, j)
                oper[j] += 1

    return


max_result = -1e9
min_result = 1e9
n = int(input())

numbers_list = list(map(int, input().split()))

oper = list(map(int, input().split()))

dfs(1, numbers_list[0], 0, 0)

print(max_result)
print(min_result)
