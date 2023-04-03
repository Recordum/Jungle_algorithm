import sys
from collections import deque
input = sys.stdin.readline



def bfs():
    q = deque([])
    q.append([0,0,field[0][0]])
    visited[0][0] = True
    dp[0][0] = field[0][0]
    dr = [0, 1, 0, -1]
    dc = [1, 0 ,-1 ,0]

    while q:
        row, col, cost = q.popleft()
        if row == n-1 and col == n-1:
            continue
        for i in range(4):
            new_row = row + dr[i]
            new_col = col + dc[i]
            if new_row < 0 or n <= new_row or new_col < 0 or n <= new_col:
                continue
            if dp[new_row][new_col] <= cost + field[new_row][new_col]:
                continue
            dp[new_row][new_col] = cost + field[new_row][new_col]
            q.append([new_row,new_col,cost + field[new_row][new_col]])
    return

result = []
while True:
    n = int(input())
    if n == 0:
        break
    field = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    dp = [[1e9]*n for _ in range(n)]
    bfs()
    result.append(dp[n-1][n-1])

for i in range(len(result)):
    print("Problem " + str(i+1) + ": " + str(result[i]))