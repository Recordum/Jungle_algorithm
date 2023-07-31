import sys
input = sys.stdin.readline


def divide_conq(row, col, length):
    if length >= 3:
        for i in range(3):
            for j in range(3):
                if i == j and i//2 == 0 and i != 0:
                    continue
                divide_conq(row + length//3 * i , col + length//3 * j, length//3)
    
    star_map[row][col] = "*"

n = int(input())
star_map = [[" "] * n for _ in range(n)]
divide_conq(0, 0, n)

for i in range(n):
    for j in range(n):
        print(star_map[i][j], end="")
    print()