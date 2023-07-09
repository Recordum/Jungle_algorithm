import sys
from collections import deque
input = sys.stdin.readline


def bfs(row, col):
    global length
    global result
    q = deque([])
    q.append([row,col,0])
    while(q):
        row, col, count = q.popleft()
        if count == length:
            result += 1
        for i in range(4):
            new_row = row + dr[i]
            new_col = col + dc[i]
            if row < 0 or row >= 4 or col < 0 or col>=3 :
                continue
            if not visited[new_row][new_col] and password[new_row][new_col] != -1:
                visited[new_row][new_col] = True
                q.append([new_row, new_col, count + 1])

    return
t = int(input())

password = [[0] * 3 for _ in range(4)]
x = 1
for i in range(4):
    for j in range(3):
        password[i][j] = x
        x+=1
password[3][0] = 0
password[3][1] = -1
password[3][2] = -1
visited = [[False] * 3 for _ in range(4)]
total = []
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
for _ in range(t):
    result = 0
    length = int(input())
    for i in range(4):
        for j in range(3):
            if password[i][j] == -1:
                continue
            bfs(i,j)
    total.append(result)

print(total)