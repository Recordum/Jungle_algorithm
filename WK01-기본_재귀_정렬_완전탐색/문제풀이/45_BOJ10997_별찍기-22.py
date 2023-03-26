import sys
input = sys.stdin.readline

def star_recursion(depth, row, col, start_row, start_col):
    if depth == 1:
        return

    for j in range(start_col, col):
        field[start_col][j] = "*"
        field[row-1][j] = "*"
    for i in range(start_row, row):
        field[i][start_row] = "*"
    for i in range(start_row + 2, row):
        field[i][col-1] = "*"
    for j in range(start_col + 2, col):
        field[start_row+2][j] = "*"
    for i in range(start_row + 2, row -2):
        field[i][start_col + 2] = "*"

    return star_recursion(depth-1, row-2 , col -2 ,start_row + 2, start_col + 2)


n = int(input())
field = list([' '] * (4*n-3) for i in range(4*n-1))
if n ==1 :
    print("*")
    exit()
star_recursion(n, 4*n-1, 4*n-3, 0, 0)

for i in range(len(field)):
    for j in range(len(field[i])):
        if i == 1 and field[i][j] == ' ':
            break
        print(field[i][j],end="")
    print()