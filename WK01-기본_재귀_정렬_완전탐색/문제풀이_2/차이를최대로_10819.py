import sys
input = sys.stdin.readline

def diff_recursion(depth, current_index , value):
    global result

    visited[current_index] = True

    if depth == n:
        result = max(result,value)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            diff_recursion(depth+1, i , value + abs(numbers_list[current_index] - numbers_list[i]))
            visited[i] = False
    return




result = 0
n = int(input())
result = 0
new_numbers = []
numbers_list = list(map(int,input().split()))
for i in range(n):
    visited = [False]*n
    diff_recursion(1,i, 0)

print(result)

