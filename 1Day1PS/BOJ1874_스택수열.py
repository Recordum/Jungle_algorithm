import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]
stack = []
result = []
current = 1
for element in sequence:
    while current <= element:
        result.append("+")
        stack.append(current)
        current += 1

    if stack[-1] == element:
        stack.pop()
        result.append("-")
    elif element < current:
        print("NO")
        exit(0)

for res in result:
    print(res)

