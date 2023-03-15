import sys
input = sys.stdin.readline

def binary_search(start,end):
    global k
    mid = (start+end)//2
    count = 0
    if start > end:
        return end

    for line in line_list:
        count += line // mid

    if count < n:
        return binary_search(start, mid -1)
    else:
        return binary_search(mid+1, end)

k, n = map(int,input().split())

line_list = sorted([int(input()) for _ in range(k)])
print(binary_search(1, line_list[-1]))