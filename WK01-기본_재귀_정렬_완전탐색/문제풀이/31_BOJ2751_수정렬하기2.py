import sys
input = sys.stdin.readline

t = int(input())

numbers = []

for i in range(t):
    numbers.append(int(input()))

sorted_numbers = sorted(numbers)

for sorted_number in sorted_numbers:
    print(sorted_number)