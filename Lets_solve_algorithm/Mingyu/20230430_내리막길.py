import sys
input = sys.stdin.readline


def dfs(row, col):
    global count

    if row == n-1 and col == m-1:
        count += 1
        return
    for i in range(4):
        if 0 > row + dr[i] or row + dr[i] >= n or 0 > col + dc[i] or col + dc[i] >= m:
            continue
        if not visited[row + dr[i]][col + dc[i]] :
            if filed[row][col] > filed[row+dr[i]][col + dc[i]]:
                visited[row + dr[i]][col + dc[i]] = True
                dfs(row+dr[i], col+dc[i])
                visited[row + dr[i]][col + dc[i]] = False



n ,m = map(int,input().split())
count = 0
filed = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]
dp_matrix = [[0] * m for _ in range(n)]
dr = [1, 0, -1 ,0]
dc = [0, 1, 0, -1]
visited[0][0] = True
dfs(0,0)
print(count)
