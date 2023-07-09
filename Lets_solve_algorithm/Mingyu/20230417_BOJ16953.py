import sys
input = sys.stdin.readline

a, b = map(str, input().split())
count = 1
while True:
    if a == b or int(a) > int(b):
        break
    if b[-1] == '1':
        b = b[:len(b)-1]
        count += 1
    else:
        if int(b) % 2 == 0:
            b = str(int(b) // 2)
            count += 1
        else:
            print(-1)
            exit(0)

if a == b:
    print(count)
else:
    print(-1)