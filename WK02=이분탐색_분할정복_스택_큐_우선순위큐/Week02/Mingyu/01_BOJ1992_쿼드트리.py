import sys
input = sys.stdin.readline


def is_same(length, start_row, start_col):
    number = field[start_row][start_col]
    for i in range(start_row, start_row + length):
        for j in range(start_col, start_col +length):
            if number != field[i][j]:
                return False
    if number == 1:
        result.append(str(1))
    else:
        result.append(str(0))
    return True

def divide_con(length, start_row, start_col):
    if not is_same(length,start_row,start_col):
        result.append('(')
        divide_con(length//2, start_row, start_col)
        divide_con(length//2, start_row, start_col + length//2)
        divide_con(length//2, start_row + length//2, start_col)
        divide_con(length//2, start_row + length//2 , start_col + length//2)
        result.append(')')
    return

result = []
n = int(input())
field = []
for _ in range(n):
    field_r = input()
    field.append([int(field_r[i]) for i in range(n)])
divide_con(n, 0, 0)

print("".join(result))
