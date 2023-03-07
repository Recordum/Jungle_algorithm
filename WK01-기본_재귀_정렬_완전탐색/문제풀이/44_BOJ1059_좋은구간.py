import sys
input = sys.stdin.readline

l = int(input())
numbers = sorted(list(map(int, input().split())))

n = int(input())

for number in numbers:
    if n == number:
        print(0)
        exit()
    if n > number:
        min_number = number + 1
    if n < number:
        max_number = number - 1
        break

if n < numbers[0]:
    min_number = 1

result = (n - min_number) * (max_number - n + 1) + max_number - n

print(result)
