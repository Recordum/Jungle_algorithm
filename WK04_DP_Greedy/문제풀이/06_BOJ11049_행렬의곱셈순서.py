import sys
input = sys.stdin.readline

n = int(input())
matrix_list = [list(map(int, input().split())) for _ in range(n)]
dp_matrix = [[0] * n for _ in range(n)]
element = [0] * (n+1)
element[0] = matrix_list[0][0]
element[1] = matrix_list[0][1]
for i in range(2, len(element)):
    element[i] = matrix_list[i-1][1]

for i in range(1, n):
    for row in range(n):
        col = row + i
        if col >= n:
            break
        dp_matrix[row][col] = 2**31
        for k in range(row, col):
            dp_matrix[row][col] = min(dp_matrix[row][col],dp_matrix[row][k]+dp_matrix[k+1][col]+ element[row] * element[k+1] * element[col + 1])

print(dp_matrix[0][n-1])
