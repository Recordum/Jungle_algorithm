import sys
input = sys.stdin.readline
def is_validate_location(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def dfs_queen(row_number):
    global result
    if row_number == n:
        result += 1
        return
    else:
        for i in range(n):
            row[row_number] = i
            if is_validate_location(row_number):
                dfs_queen(row_number + 1)


if __name__ == '__main__':
    n = int(input())
    result = 0
    row = [0] * n
    dfs_queen(0)
    print(result)