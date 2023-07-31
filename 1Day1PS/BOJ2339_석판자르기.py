import sys 
input = sys.stdin.readline

def find_impurity(start_row, start_col, row, col):
    for i in (start_row, row):
        for j in (start_col, col):
            if stone[i][j] == 1:
                return i,j 

def cut_stone(row, col, length):
    r, c = find_impurity(row ,col, row + length, col + length)
    
    for i in range(row, row + length):
        if stone[i, c] == 2:
            break
        
    for j in range(col, col + length):
        if stone[r, j] == 2:
            break


n = int(input())

stone = [[map(int, input().split())] for _ in range(n)]
cut_stone(row, col, length)