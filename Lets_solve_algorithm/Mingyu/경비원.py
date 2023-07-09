import sys
input = sys.stdin.readline


col, row = map(int, input().split())
number = int(input())

location = [map(int, input().split()) for _ in range(number)]

start_direction, start_distance = map(int, input().split())
total_distance = 0
for i in range(number):
    direction, distance = location[i]
    if direction == start_direction:
        total_distance += abs(start_distance - distance)
        continue
    if start_direction == 1:
        if direction == 2:
            total_distance += row + min(start_distance + distance, 2 * col - start_distance - distance)
            continue
        if direction == 3:
            total_distance += distance + start_distance
            continue
        if direction == 4:
            total_distance += col - start_distance + distance
            continue
    if start_direction == 2:
        if direction == 1:
            total_distance += row + min(start_distance + distance, 2 * col - start_distance - distance)
            continue
        if direction == 3:
            total_distance += start_distance + row - distance
            continue
        if direction == 4:
            total_distance += col - start_distance + row - distance
            continue
    if start_direction == 3:
        if direction == 1:
            total_distance += distance + start_distance
            continue
        if direction == 2:
            total_distance += distance + col - start_distance
            continue
        if direction == 4:
            total_distance += col + min(start_distance + distance, 2 * row - start_distance - distance)
            continue
    if start_direction == 4:
        if direction == 1:
            total_distance += col - distance + start_distance
            continue
        if direction == 2:
            total_distance += row - start_distance + col - distance
            continue
        if direction == 3:
            total_distance += col + min(start_distance + distance, 2 * row - start_distance - distance)
            continue

print(total_distance)


