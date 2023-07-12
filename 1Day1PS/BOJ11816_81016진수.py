import sys
input = sys.stdin.readline

x = str(input().rstrip())

if "x" in x:
    result = int(x, 16)
elif x[0] == "0" and len(x) > 1:
    result = int(x, 8)
else:
    result = int(x)

print(result)

