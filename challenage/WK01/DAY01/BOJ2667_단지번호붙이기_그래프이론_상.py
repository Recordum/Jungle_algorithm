import sys
# 정답 / 실버 1
# 전형적인 DFS/BFS문제 
# DFS 알고리즘 에서 시작지점을 방문체크를 해줘야함을 유의해야함
def dfs(start_row, start_col, count):
    global n
    field[start_row][start_col] = 0
    dr = [1, 0, -1 ,0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        row = dr[i] + start_row
        col = dc[i] + start_col
        if row < 0 or row >= n or col < 0 or col >= n:
            continue
        if field[row][col] == 0:
            continue
        count = dfs(row, col, count + 1)
    return count

n = int(input())
field = [list(map(int, input())) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if field[i][j] == 1:
            result.append(dfs(i,j,1))

print(len(result))
result.sort()
for ans in result:
    print(ans)

