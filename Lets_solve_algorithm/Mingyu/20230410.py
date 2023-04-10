import sys
from collections import deque
input = sys.stdin.readline



def bfs(row, col):
    global flag
    visited[row][col] = True
    q = deque([])
    q.append([row,col,0])
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    field[row][col] = -1
    while q:
        row, col, count = q.popleft()
        if 2 < field[row][col] <= 5 :
            flag = True
            return count
        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]
            if 0<=n_row<n and 0<= n_col<m:
                if field[n_row][n_col] != 1 and field[n_row][n_col] != -1:
                    if 2 < field[n_row][n_col] <= 5:
                        flag = True
                        count += 1
                        return count
                    field[n_row][n_col] = -1
                    q.append([n_row, n_col, count+1])

    return count

flag = False
n,m = map(int, input().split())
field = [list(map(int,(input().rstrip()))) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
result = 0
row = 0
col = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == 2:
            row = i
            col = j
            break
result = bfs(row, col)

if flag:
    print("TAK")
    print(result)
else:
    print("NIE")


