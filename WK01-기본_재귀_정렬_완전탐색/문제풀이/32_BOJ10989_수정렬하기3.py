import sys
input = sys.stdin.readline

t = int(input())

count = [0] * 10001

for i in range(t):
    number = int(input())
    count[number] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
