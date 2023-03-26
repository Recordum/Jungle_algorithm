import sys
input = sys.stdin.readline

def binary_search(start,end):
    mid = (start+end)//2
    house_stack = []
    if end < start:
        return end

    for house in house_list:
        if not house_stack:
            house_stack.append(house)
            continue
        if house - house_stack[-1] < mid:
            continue
        if house - house_stack[-1] >= mid:
            house_stack.append(house)



    if len(house_stack) < c:
        return binary_search(start, mid-1)

    if len(house_stack) >= c:
        return binary_search(mid+1, end)


n, c = map(int,input().split())
house_list = sorted([int(input()) for _ in range(n)])
print(binary_search(1, house_list[-1]))

