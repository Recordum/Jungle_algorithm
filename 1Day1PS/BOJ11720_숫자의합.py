import sys
input = sys.stdin.readline

n = int(input())
total = str(input().rstrip())

numbers = [int(elem) for elem in total]
print(sum(numbers))