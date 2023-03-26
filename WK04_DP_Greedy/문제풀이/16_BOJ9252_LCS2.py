import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
def back_tracking(row, col):

    if dp_matrix[row][col-1] == dp_matrix[row][col]:
        back_tracking(row, col-1)
        return
    if dp_matrix[row-1][col] == dp_matrix[row][col]:
        back_tracking(row-1, col)
        return
    if dp_matrix[row-1][col-1] == dp_matrix[row][col] -1:
        result.append(second_str[row-1])
        if not dp_matrix[row-1][col-1]:
            return
        back_tracking(row-1, col-1)

first_str = input().rstrip()
second_str = input().rstrip()

dp_matrix = [[0] * (len(first_str) + 1) for _ in range(len(second_str) + 1)]
result = []
for i in range(1, len(second_str) + 1):
    for j in range(1, len(first_str) + 1):
        if second_str[i-1] == first_str[j-1]:
            dp_matrix[i][j] = dp_matrix[i-1][j-1] + 1
            continue
        max_dp = max(dp_matrix[i-1][j], dp_matrix[i][j-1])
        if dp_matrix[i][j] < max_dp:
            dp_matrix[i][j] = max_dp
if not dp_matrix[-1][-1]:
    print(0)
    exit()
back_tracking(len(second_str) ,len(first_str))

print(dp_matrix[-1][-1])
for ans in reversed(result):
    print(ans, end ="")
