import sys
input = sys.stdin.readline

def binary_search(start, end):
    global m 
    mid = (start + end)//2
    if start > end:
        return end
    count = 0
    for network_line in network_lines:
        count += network_line//mid

    if count < m:
        return binary_search(start, mid -1)
    else:
        return binary_search(mid + 1, end)

k, m = map(int, input().split())
network_lines = [int(input()) for _ in range(k)]
network_lines.sort()
print(binary_search(1, network_lines[-1]))
