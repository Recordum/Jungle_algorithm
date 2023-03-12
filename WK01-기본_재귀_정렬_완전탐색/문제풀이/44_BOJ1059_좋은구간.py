import sys
input = sys.stdin.readline

l = int(input())
numbers = sorted(list(map(int, input().split())))

n = int(input())

for temp in numbers:
    if n == temp:
        print(0)
        exit()
    if n > temp:
        min_number = temp + 1
    if n < temp:
        max_number = temp - 1
        break

if n < numbers[0]:
    min_number = 1

result = (n - min_number) * (max_number - n + 1) + max_number - n

print(result)
