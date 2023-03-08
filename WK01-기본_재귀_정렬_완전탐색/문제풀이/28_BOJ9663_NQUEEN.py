import sys
input = sys.stdin.readline
def is_validate_location(row_number):
    for i in range(row_number):
        if row[row_number] == row[i] or abs(row[row_number] - row[i]) == abs(row_number - i):
            return False
    return True

def dfs_queen(row_number):
    global result
    if row_number == n:
        result += 1
        return

    for i in range(n):
        if not flag[row_number][i] and not marked_col[i]:
            row[row_number] = i
            if is_validate_location(row_number):
                marked_col[i] = True
                if i+1 < n and row_number + 1 < n :
                    flag[row_number + 1][i+1] = True
                if i-1 >= 0 and row_number + 1 < n :
                    flag[row_number + 1][i-1] = True
                dfs_queen(row_number + 1)
                marked_col[i] = False
                if i+1 < n and row_number + 1 < n :
                    flag[row_number + 1][i+1] = False
                if i-1 >= 0 and row_number + 1 < n :
                    flag[row_number + 1][i-1] = False


if __name__ == '__main__':
    n = int(input())
    result = 0
    flag = [[False] *n for _ in range(n)]
    marked_col = [False]*n
    row = [0] * n
    row[0]
    dfs_queen(0)
    print(result)