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

