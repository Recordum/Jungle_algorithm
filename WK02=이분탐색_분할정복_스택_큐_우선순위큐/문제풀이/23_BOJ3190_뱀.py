import sys
from collections import deque
input = sys.stdin.readline

def direction_change(flag,direction):
    if direction == "D":
        if flag == "R":
            flag = "D"
            return flag
        if flag == "U":
            flag = "R"
            return flag
        if flag == "L":
            flag = "U"
            return flag
        if flag == "D":
            flag = "L"
            return flag
    if direction == "L":
        if flag == "R":
            flag = "U"
            return flag
        if flag == "U":
            flag = "L"
            return flag
        if flag == "L":
            flag = "D"
            return flag
        if flag == "D":
            flag = "R"
            return flag



def snake_move(snake_size,current_row,current_col,current_time, flag):
    while True:
        if flag == "R":
            if current_row < 0 or current_row >= n or current_col + snake_size< 0 or current_col + snake_size>= n or [current_row, current_col + snake_size] in snake_body:
                current_time +=1
                break
            if field[current_row][current_col + snake_size] == 1:
                field[current_row][current_col + snake_size] = 0
                current_col = current_col + snake_size
                snake_body.append([current_row, current_col])

                current_time += 1

            else:
                current_col = current_col + snake_size
                snake_body.append([current_row, current_col])
                snake_body.popleft()
                current_time+=1

        if flag == "L":
            if current_row < 0 or current_row >= n or current_col - snake_size< 0 or current_col - snake_size>= n or [current_row, current_col-snake_size] in snake_body:
                current_time +=1
                break
            if field[current_row][current_col - snake_size] == 1:
                field[current_row][current_col - snake_size] = 0
                current_col = current_col - snake_size
                snake_body.append([current_row, current_col])

                current_time += 1
            else:
                current_col = current_col - snake_size
                snake_body.append([current_row, current_col])
                snake_body.popleft()
                current_time+=1

        if flag == "D":
            if current_col < 0 or current_col >= n or current_row + snake_size< 0 or current_row + snake_size>= n or [current_row + snake_size, current_col] in snake_body:
                current_time +=1
                break
            if field[current_row+snake_size][current_col] == 1:
                field[current_row+snake_size][current_col] = 0
                current_row = current_row + snake_size
                snake_body.append([current_row, current_col])

                current_time += 1

            else:
                current_row = current_row + snake_size
                snake_body.append([current_row, current_col])
                snake_body.popleft()
                current_time+=1

        if flag == "U":
            if current_col < 0 or current_col >= n or current_row - snake_size< 0 or current_row - snake_size>= n or [current_row - snake_size, current_col] in snake_body:
                current_time +=1
                break
            if field[current_row - snake_size][current_col] == 1:
                field[current_row - snake_size][current_col] = 0
                current_row = current_row - snake_size
                snake_body.append([current_row, current_col])

                current_time += 1

            else:
                current_row = current_row - snake_size
                snake_body.append([current_row, current_col])
                snake_body.popleft()
                current_time += 1

        if time_list:
            if current_time >= time_list[0]:
                time_list.popleft()
                direction = direction_list.popleft()
                flag = direction_change(flag, direction)

    return current_time

n = int(input())
field = [[0 for i in range(n)] for i in range(n)]
k = int(input())
flag = 'R'
for _ in range(k):
    apple_row, apple_col = map(int,input().split())
    field[apple_row-1][apple_col-1] = 1
l = int(input())
current_row = 0
current_col = 0
snake_size = 1
start_time = 0
time_list = deque([])
direction_list = deque([])
snake_body = deque([[0,0]])
for _ in range(l):
    time, direction = map(str, input().split())
    time_list.append(int(time))
    direction_list.append(direction)

print(snake_move(snake_size,current_row,current_col,start_time,flag))

