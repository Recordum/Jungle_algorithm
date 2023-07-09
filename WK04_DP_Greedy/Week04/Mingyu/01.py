import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def jump(row,col):
    global count
    if row == n-1 and col == n-1:
        return 1

    if dp[row][col] > count:
        return dp[row][col]

    new_col = col + field[row][col]
    new_row = row + field[row][col]

    if 0 <= new_row < n:
        if field[new_row][col]:
            dp[row][col] += jump(new_row, col)
    if 0 <= new_col < n:
        if field[row][new_col]:
            dp[row][col] += jump(row, new_col)

    return dp[row][col]

n = int(input())
count = 0
field = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
jump(0,0)
print(dp[0][0])