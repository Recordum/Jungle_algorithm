import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(row, col, color, count):
    dr = [1, 0 , -1 , 0]
    dc = [0, 1 , 0 , -1]
    for i in range(4):
        new_row = row + dr[i]
        new_col = col + dc[i]
        if new_row >= m or new_row < 0 or new_col >= n or new_col < 0 :
            continue
        if battle_filed[new_row][new_col] == color and not visited[new_row][new_col]:
            visited[new_row][new_col] = True
            count = dfs(new_row,new_col,color, count + 1)
    return count

n, m = map(int, input().split())
whilte_count = 0
blue_count = 0
battle_filed = [list(map(str, input())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if battle_filed[i][j] == 'W':
                visited[i][j] = True
                whilte_count += dfs(i,j,'W', 1) ** 2
            else:
                visited[i][j] = True
                blue_count += dfs(i,j,'B', 1) ** 2

print(whilte_count, blue_count)
