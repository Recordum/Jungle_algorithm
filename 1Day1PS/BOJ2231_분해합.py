import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    number = list(map(int,str(i)))
    if n - i - sum(number) == 0:
        print(i)
        exit(0)

print(0)