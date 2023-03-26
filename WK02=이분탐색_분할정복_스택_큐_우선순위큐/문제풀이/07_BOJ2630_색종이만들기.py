import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def same_paper(row, col, start_row, start_col):
    init_color = paper[start_row][start_col]
    for i in range(start_row, row+ start_row):
        for j in range(start_col , col + start_col):
            if paper[i][j] != init_color:
                return False
    return True

def divide_paper(row_length, col_lenth, start_row, start_col):
    global count_white
    global count_blue
    if not same_paper(row_length, col_lenth,  start_row, start_col):
        divide_paper(row_length // 2, col_lenth // 2, start_row, start_col)
        divide_paper(row_length // 2, col_lenth // 2, start_row, start_col + col_lenth//2)
        divide_paper(row_length // 2, col_lenth // 2, start_row + row_length//2, start_col)
        divide_paper(row_length // 2, col_lenth // 2, start_row + row_length//2, start_col + col_lenth//2)
    else:
        if paper[start_row][start_col] == 1:
            count_blue += 1
        else:
            count_white += 1
    return


n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
count_white = 0
count_blue = 0
divide_paper(n, n , 0, 0)
print(count_white)
print(count_blue)