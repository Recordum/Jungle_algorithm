import sys
input = sys.stdin.readline


def divide_star(length, row, col):

    for i in range(col, col + length):
        star_map[row][i] = "*"
        star_map[length+row-1][i] = "*"
    for j in range(row, row + length):
        star_map[j][col] = "*"
        star_map[j][length + col - 1] = "*"

    if length == 3:
        return

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            divide_star(length//3, row + i * length//3, col + j * length//3)



n = int(input())
star_map = [[" "]*n for i in range(n)]
divide_star(n,0,0)
for i in range(n):
    for j in range(n):
        print(star_map[i][j], end="")
    print()