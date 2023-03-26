import sys
input = sys.stdin.readline

split_by_minus = input().rstrip().split('-')

before_minus = list(map(int, split_by_minus[0].split("+")))
number = sum(before_minus)
for i in range(1, len(split_by_minus)):
    temp = list(map(int,split_by_minus[i].split('+')))
    number -= sum(temp)

print(number)