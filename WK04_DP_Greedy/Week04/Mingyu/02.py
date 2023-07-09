import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs():

    q = deque([])
    q.append([0,0])
    while q:
        row, col ,count = q.popleft()
        for i in range(4):
            new_col = col + dcol[i]
            new_row = row + drow[i]
            if new_row < 0 or n-1 < new_row or new_col < 0 or n-1 < new_col:
                continue
            if dp[row][col] != -1:
                continue
            if field[new_row][new_col] < field[col][row]:
                dp[row][col] += 1
            q.append([new_row,new_col])
    return

drow = [1,0,-1,0]
dcol = [0,1,0,-1]
n = int(input())
field = [list(map(int,input().split()))]
dp = [[-1] * n for _ in range(n)]
visited = [[False]]