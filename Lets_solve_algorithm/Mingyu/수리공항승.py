import sys
input = sys.stdin.readline

n, l = map(int, input().split())
locate = list(map(int, input().split()))
locate.sort()
result = 1
start = 0
next = 1

if len(locate) < 2 :
    print(1)
    exit(0)

for _ in range(1, len(locate)):
    if locate[next] + 0.5 - locate[start] + 0.5 <= l:

        next += 1
        continue
    result += 1
    start = next
    next += 1

print(result)

