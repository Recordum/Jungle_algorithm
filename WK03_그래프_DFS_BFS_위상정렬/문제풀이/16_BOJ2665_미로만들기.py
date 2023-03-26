import heapq
import sys

def bfs_heap():
    global result
    hq = []
    heapq.heappush(hq, [0,0,0])
    visited[0][0] = True
    while hq:
        wall, row, col = heapq.heappop(hq)
        for i in range(4):
            next_row = row + d_row[i]
            next_col = col + d_col[i]
            if not (0<=next_row<n and 0<=next_col<n):
                continue
            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                if maze[next_row][next_col] == 0:
                    heapq.heappush(hq, [wall + 1,next_row, next_col])
                else :
                    heapq.heappush(hq, [wall, next_row, next_col])
            if next_row == n-1 and next_col == n-1:
                return wall
    return



flag = 0
d_row = [1,0,-1,0]
d_col = [0,1,0,-1]
end_row = 0
end_col = 0
n = int(input())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
result = bfs_heap()
print(result)