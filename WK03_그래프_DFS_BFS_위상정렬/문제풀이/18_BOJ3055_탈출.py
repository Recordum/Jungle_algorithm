import sys
from collections import deque
input = sys.stdin.readline



def check_location(q_flood, q_hedge):
    for i in range(r):
        for j in range(c):
            if field[i][j] == 'S':
                visited_hedge[i][j] = True
                q_hedge.append([i,j,0])
                continue
            if field[i][j] == '*':
                visited_flood[i][j] = True
                q_flood.append(([i,j]))
                continue
    return

def dfs():
    q_flood = deque([])
    q_hedge = deque([])
    check_location(q_flood, q_hedge)
    while q_hedge:
        for _ in range(len(q_flood)):
            row_flood, col_flood = q_flood.popleft()
            for i in range(4):
                new_row_flood = row_flood + dr[i]
                new_col_flood = col_flood + dc[i]
                if not(0 <= new_row_flood < r and 0 <= new_col_flood < c):
                    continue
                if not visited_flood[new_row_flood][new_col_flood] and not field[new_row_flood][new_col_flood] == 'D' and not field[new_row_flood][new_col_flood] == 'X':
                    visited_flood[new_row_flood][new_col_flood] = True
                    q_flood.append([new_row_flood, new_col_flood])
        for _ in range(len(q_hedge)):
            row_hedge, col_hedge, count = q_hedge.popleft()
            for i in range(4):
                new_row_hedge = row_hedge + dr[i]
                new_col_hedge = col_hedge + dc[i]
                if not(0 <= new_row_hedge < r and 0 <= new_col_hedge < c):
                    continue
                if field[new_row_hedge][new_col_hedge] == 'D':
                    count += 1
                    return count
                if not visited_flood[new_row_hedge][new_col_hedge] and not visited_hedge[new_row_hedge][new_col_hedge] and not field[new_row_hedge][new_col_hedge] == 'X':

                    visited_hedge[new_row_hedge][new_col_hedge] = True
                    q_hedge.append([new_row_hedge, new_col_hedge, count + 1])
    return "KAKTUS"

dr = [1,0,-1,0]
dc = [0,1,0,-1]
r, c = map(int,input().split())
field = [list(input().rstrip()) for _ in range(r)]
visited_flood = [[False for _ in range(c)] for _ in range(r)]
visited_hedge = [[False for _ in range(c)] for _ in range(r)]
print(dfs())
