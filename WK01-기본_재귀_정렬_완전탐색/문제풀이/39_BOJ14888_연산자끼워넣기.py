import sys
input = sys.stdin.readline

def dfs(previous_result, next_number , current_operation, depth):

    global min_answer
    global max_answer
    if operation_list[current_operation] == 0:
        return

    if current_operation == 0 and next_number < n:
        previous_result = previous_result + a[next_number]
    if current_operation == 1 and next_number < n:
        previous_result = previous_result - a[next_number]
    if current_operation == 2 and next_number < n:
        previous_result = int(previous_result * a[next_number])
    if current_operation == 3 and next_number < n:
        if previous_result < 0:
            previous_result = -((-previous_result) // a[next_number])
        else:
            previous_result = previous_result // a[next_number]

    if depth == n -1:
        if min_answer > previous_result:
            min_answer = previous_result
        if max_answer < previous_result:
            max_answer = previous_result
        return

    operation_list[current_operation] -= 1
    for i in range(4):
        dfs(previous_result, next_number + 1, i, depth+1 )
    operation_list[current_operation] += 1
    return

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    operation_list = list(map(int, input().split()))
    max_answer = int(-1e9)
    min_answer = int(1e9)
    for i in range(4):
        dfs(a[0],1,i,1)

    print(max_answer)
    print(min_answer)




