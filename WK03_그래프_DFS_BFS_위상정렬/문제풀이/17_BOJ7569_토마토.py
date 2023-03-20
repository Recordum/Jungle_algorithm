import sys
from collections import deque
input = sys.stdin.readline


def ripe_tomato(q):
    for i in range(len(box)):
        for j in range(len(box[i])):
            for k in range(len(box[i][j])):
                if box[i][j][k] == 1:
                    visited[i][j][k] = True
                    q.append([j,k,i,0])


def is_ripe():
    for i in range(len(box)):
        for j in range(len(box[i])):
            for k in range(len(box[i][j])):
                if box[i][j][k] == 0:
                    return False
    return True


def dfs_tomato():
    q = deque([])
    ripe_tomato(q)
    while q:
        row, col, height, count = q.popleft()
        for i in range(6):
            new_row = row + dr[i]
            new_col = col + dc[i]
            new_height = height + dh[i]
            if not(0 <= new_row < n and 0 <= new_col < m and 0 <= new_height < h):
                continue
            if not visited[new_height][new_row][new_col] and box[new_height][new_row][new_col] == 0:
                box[new_height][new_row][new_col] = 1
                visited[new_height][new_row][new_col] = True
                q.append([new_row, new_col, new_height, count + 1])
    if not is_ripe():
        count = -1
    return count

dr = [1,0,-1,0,0,0]
dc = [0,1,0,-1,0,0]
dh = [0,0,0,0,1,-1]
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
print(dfs_tomato())