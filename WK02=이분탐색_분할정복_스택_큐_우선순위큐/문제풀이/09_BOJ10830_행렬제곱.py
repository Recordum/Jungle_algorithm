import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def matrix_multiply(matrix_a, matrix_b):
    new_list = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_list[i][j] += matrix_a[i][k] * matrix_b[k][j]
            new_list[i][j] = new_list[i][j] % 1000

    return new_list

def matrix_exp(a_list, b):
    if b == 1:
        return a_list

    matrix_value = matrix_exp(a_list, b // 2)

    temp_matrix = matrix_multiply(matrix_value,matrix_value)

    if b % 2 != 0:
        temp_matrix = matrix_multiply(temp_matrix, a_list)

    return temp_matrix


n,b = map(int,input().split())
a_list = [list(map(int,input().split())) for _ in range(n)]
if b == 1:
    result = [[a_list[i][j] % 1000 for j in range(n)] for i in range(n)]
else :
    result = matrix_exp(a_list, b)
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    if i == j == n-1:
        exit()
    print()

