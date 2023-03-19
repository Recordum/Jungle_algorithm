import sys
from collections import deque
input = sys.stdin.readline

def bfs(row,col):
    q = deque([])
    q.append([row, col])
    visited[row][col] = True
    depth[row][col] = 1
    while q:
        row, col = q.popleft()
        for i in range(4):
            if row + d_row[i] < 0 or row + d_row[i] >= n or col + d_col[i] < 0 or col + d_col[i] >= m :
                continue
            if not visited[row + d_row[i]][col + d_col[i]] and maze[row + d_row[i]][col + d_col[i]] != 0:
                visited[row + d_row[i]][col + d_col[i]] = True
                depth[row + d_row[i]][col + d_col[i]] = depth[row][col] + 1
                if row + d_row[i] == n-1 and col + d_col[i] == m-1:
                    return depth[row + d_row[i]][col + d_col[i]]
                q.append([row+d_row[i], col + d_col[i]])
    return

d_row = [1,0,-1,0]
d_col = [0,1,0,-1]
n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n) ]
depth = [[0 for _ in range(m)] for _ in range(n) ]
maze = [list(map(int, input().rstrip())) for _ in range(n)]
print(bfs(0,0))
