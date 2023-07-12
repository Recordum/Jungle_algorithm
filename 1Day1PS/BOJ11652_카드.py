import sys
input = sys.stdin.readline

numberMap = {}
n = int(input())
for _ in range(n):
    number = int(input())
    if (number in numberMap):
        numberMap[number] += 1
    else:
        numberMap[number] = 1

max_value = max(numberMap.values())
results = [key for key, value in numberMap.items() if value == max_value]

print(min(results))
