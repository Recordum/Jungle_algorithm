import sys
from collections import deque
input = sys.stdin.readline

def divide(row, col):
    global continent
    if field[row][col] != 1:
        return
    q = deque([])
    q.append([row, col])
    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow = row + d_row[i]
            ncol = col + d_col[i]
            if nrow < 0 or nrow >= n or ncol < 0 or ncol >= n:
                continue
            if not visited[nrow][ncol]:
                if field[nrow][ncol] == 1:
                    visited[nrow][ncol] = True
                    field[nrow][ncol] = continent
                    q.append([nrow, ncol])
    continent += 1
    return
n = int(input())
field = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
continent = 1
d_row = [1,0,-1,0]
d_col = [0,1,0,-1]
for i in range(n):
    for j in range(n):
            divide(i,j)

visited = [[False]*n for _ in range(n)]
print("end")