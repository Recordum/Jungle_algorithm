import sys
input = sys.stdin.readline

def validate_loc(row_index) :
    for i in range(row_index):
        if row[i] == row[row_index] or abs(i - row_index) == abs(row[i] - row[row_index]):
            return False
    return True

def queen_dfs(row_index):
    global count
    if row_index == n:
        count += 1
        return

    for col_index in range(n):
        if not marked_col[col_index]:
            row[row_index] = col_index

            if validate_loc(row_index):
                marked_col[col_index] = True
                queen_dfs(row_index+1)
                marked_col[col_index] = False


count = 0
n = int(input())
marked_col = [False]*n
row = [0] * n
queen_dfs(0)
print(count)