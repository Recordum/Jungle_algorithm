import sys
input = sys.stdin.readline

def binary_search(start, end):
    global result
    mid = (start + end) //2
    value = 0
    if end < start:
        return

    for level in level_list:
        if mid > level:
            value += mid - level

    if value > k:
        return binary_search(start, mid -1)
    else :
        result = max(result,mid)
        return binary_search(mid + 1, end)

result = 0
n, k = map(int, input().split())
level_list = sorted([int(input()) for _ in range(n)])
binary_search(level_list[0], level_list[-1] + k)
print(result)
