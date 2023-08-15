import sys
input = sys.stdin.readline

self_number = [True] * 10001

for i in range(1, 10001):
    unit = list(map(int, str(i)))
    total = sum(unit) + i
    if total < 10001:
        self_number[total] = False

for i in range(1, 10001):
    if self_number[i]:
        print(i)
