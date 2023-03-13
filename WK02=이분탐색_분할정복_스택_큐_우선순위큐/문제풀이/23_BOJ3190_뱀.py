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
    for i in range(l):
        end_time = time_list[i]
        direction = direction_list[i]
        while current_time <= end_time:
            if flag == 'R':
                if current_col + snake_size < 0 or current_col + snake_size >= n:
                    return current_time
                for snake in snake_body:
                    if snake[0] == current_row and snake[1] == current_col + snake_size:
                        return current_time
                if field[current_row][current_col+ snake_size] == 1:
                    current_col += snake_size
                    snake_size += 1
                    snake_body.append([current_row, current_col])
                else:
                    current_col += snake_size
                    snake_body.append([current_row, current_col])
                    snake_body.popleft()

            if flag == 'L':
                if current_col - snake_size < 0 or current_col - snake_size >= n:
                    return current_time
                for snake in snake_body:
                    if snake[0] == current_row and snake[1] == current_col - snake_size:
                        return current_time
                if field[current_row][current_col- snake_size] == 1:
                    current_col -= snake_size
                    snake_size += 1
                    snake_body.append([current_row, current_col])

                else:
                    current_col -= snake_size
                    snake_body.append([current_row, current_col])
                    snake_body.popleft()

            if flag == 'U':
                if current_row - snake_size < 0 or current_row - snake_size >= n:
                    return current_time

                for snake in snake_body:
                    if snake[0] == current_row - snake_size and snake[1] == current_col :
                        return current_time

                if field[current_row - snake_size][current_col] == 1:
                    current_row -= snake_size
                    snake_size += 1
                    snake_body.append([current_row, current_col])

                else:
                    current_row -= snake_size
                    snake_body.append([current_row, current_col])
                    snake_body.popleft()

            if flag == 'D':
                if current_row + snake_size < 0 or current_row + snake_size >= n:
                    return current_time
                for snake in snake_body:
                    if snake[0] == current_row + snake_size and snake[1] == current_col:
                        return current_time

                if field[current_row + snake_size][current_col] == 1:
                    current_row += snake_size
                    snake_size += 1
                    snake_body.append([current_row, current_col])

                else:
                    current_row += snake_size
                    snake_body.append([current_row, current_col])
                    snake_body.popleft()
            current_time += 1

        flag = direction_change(flag, direction)

    while True:
        if flag == 'R':
            if current_col + snake_size < 0 or current_col + snake_size >= n:
                return current_time
            for snake in snake_body:
                if snake[0] == current_row and snake[1] == current_col + snake_size:
                    return current_time

            if field[current_row][current_col + snake_size] == 1:
                current_col += snake_size
                snake_size += 1
                snake_body.append([current_row, current_col])

            else:
                current_col += snake_size
                snake_body.append([current_row, current_col])
                snake_body.popleft()

        if flag == 'L':
            if current_col - snake_size < 0 or current_col - snake_size >= n:
                return current_time
            for snake in snake_body:
                if snake[0] == current_row and snake[1] == current_col - snake_size:
                    return current_time

            if field[current_row ][current_col- snake_size] == 1:
                current_col -= snake_size
                snake_size += 1
                snake_body.append([current_row, current_col])

            else:
                current_col -= snake_size
                snake_body.append([current_row, current_col])
                snake_body.popleft()

        if flag == 'U':
            if current_row - snake_size < 0 or current_row - snake_size >= n:
                return current_time

            for snake in snake_body:
                if snake[0] == current_row - snake_size and snake[1] == current_col :
                    return current_time

            if field[current_row - snake_size][current_col] == 1:
                current_row -= snake_size
                snake_size += 1
                snake_body.append([current_row, current_col])

            else:
                current_row -= snake_size
                snake_body.append([current_row, current_col])
                snake_body.popleft()

        if flag == 'D':
            if current_row + snake_size < 0 or current_row + snake_size >= n:
                return current_time
            for snake in snake_body:
                if snake[0] == current_row + snake_size and snake[1] == current_col:
                    return current_time

            if field[current_row + snake_size][current_col] == 1:
                current_row += snake_size
                snake_size += 1
                snake_body.append([current_row, current_col])

            else:
                current_row += snake_size
                snake_body.append([current_row, current_col])
                snake_body.popleft()

        current_time += 1

n = int(input())
field = [[0 for i in range(n)] for i in range(n)]
k = int(input())
flag = 'R'
for _ in range(k):
    apple_row, apple_col = map(int,input().split())
    field[apple_row][apple_col] = 1
l = int(input())
current_row = 0
current_col = 0
snake_size = 1
start_time = 1
time_list = []
direction_list = []
snake_body = deque([[0,0]])
for _ in range(l):
    time, direction = map(str, input().split())
    time_list.append(int(time))
    direction_list.append(direction)

print(snake_move(snake_size,current_row,current_col,start_time,flag))

