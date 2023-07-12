import sys
input = sys.stdin.readline

result = []

number = int(input())

while True:
    for x in range(2, number+1):
        if number % x == 0:
            number = number // x
            result.append(x)
            break
    if number == 1:
        break

for res in result:
    print(res)
