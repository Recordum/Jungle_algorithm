import sys
input = sys.stdin.readline


def dfs(start_row, start_col, depth, row, col):
    global result
    result = max(depth, result)
    for i in range(4):
        new_row = start_row + dr[i]
        new_col = start_col + dc[i]
        if new_col < 0 or new_col >= col or new_row < 0 or new_row >= row:
            continue
        if not visited[ord(field[new_row][new_col])]:
            visited[ord(field[new_row][new_col])] = True
            dfs(new_row, new_col, depth + 1,row, col)
            visited[ord(field[new_row][new_col])] = False
    return

row, col = map(int, input().split())
field = [input().rstrip() for _ in range(row)]
visited = [False] * 100
dr = [-1,0,1,0]
dc = [0,1,0,-1]
result = 0
# print(ord("A"))
visited[ord(field[0][0])] = True
dfs(0,0,1, row, col)
print(result)
