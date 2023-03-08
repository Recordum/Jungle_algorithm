import sys
input = sys.stdin.readline


n = input().rstrip()

count = 0
if int(n) < 100:
    print(n)

else:
    for i in range(100, int(n) + 1):
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            count += 1

    print(count + 99)