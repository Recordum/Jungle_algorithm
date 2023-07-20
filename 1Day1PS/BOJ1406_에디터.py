import sys

input = sys.stdin.readline

contents = list(input().rstrip())
split_by_cursor = []
n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == 'L':
        if contents:
            split_by_cursor.append(contents.pop())

    elif command[0] == 'D':
        if split_by_cursor:
            contents.append(split_by_cursor.pop())

    elif command[0] == 'B':
        if contents:
            contents.pop()

    elif command[0] == 'P':
        contents.append(command[1])

contents += reversed(split_by_cursor)
print(''.join(contents))
