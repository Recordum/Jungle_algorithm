import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
def dfs(row, col):
    melting_count = 0
    if visited[row][col]:
        return
    visited[row][col] = True
    for i in range(4):
        if row + n_row[i] < 0 or row + n_row[i] > n - 1 or col + n_col[i] < 0 or col + n_col[i] > m -1:
            continue
        if field[row + n_row[i]][col + n_col[i]] <= 0 and not visited[row + n_row[i]][col + n_col[i]]:
            melting_count += 1
    melting_index.append([row,col,melting_count])
    for i in range(4):
        if row + n_row[i] < 0 or row + n_row [i]> n - 1 or col + n_col[i] < 0 or col + n_col[i] > m -1:
            continue
        if field[row + n_row[i]][col + n_col[i]] > 0:
            dfs(row + n_row[i], col + n_col[i])
    return True


n, m, = map(int, input().split())
n_row = [1,0,-1,0]
n_col = [0,-1,0,1]
field = [list(map(int, input().split())) for _ in range(n)]
count = 0
result = 0
while count < 2:
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0
    melting_index = []
    for row in range(n):
        for col in range(m):
            if not visited[row][col] and field[row][col] > 0:
                count += 1
                if count >= 2:
                    break
                dfs(row,col)
    if count == 0:
        print(0)
        exit()
    if count >= 2:
        break
    for row,col,melting_count in melting_index:
        field[row][col] -= melting_count

    result += 1

print(result)





