import sys
input = sys.stdin.readline

def binary_search(start, end, z):
    mid = (start + end )//2
    
    if start > end:
        return start

    if z == 100 * (y + mid) // (x + mid):
        return binary_search(mid+1, end, z)
    else:
        return binary_search(start, mid -1 ,z)


x, y = map(int, input().split())

z = 100 * y // x

result = binary_search(1, x, z)
if z >= 99:
    print(-1)
else:
    print(result)