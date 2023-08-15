import sys
input = sys.stdin.readline

def dfs(field, start_row, start_col, count):
    global n
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    field[start_row][start_col] = 0
    for i in range(4):
        row = start_row + dr[i]
        col = start_col + dc[i]
        if row < 0 or col < 0 or row >= n or col >= n:
            continue
        if field[row][col] == 0:
            continue
        
        count = dfs(field, row, col, count + 1)
    return count

n = int(input())
field = [list(map(int, input().rstrip())) for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if field[i][j] != 0:
            result.append(dfs(field, i ,j, 1))


print(len(result))
result.sort()
for ans in result:
    print(ans)

