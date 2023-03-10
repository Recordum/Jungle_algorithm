import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def binary_level(start,end):
    global result
    global k
    mid = (start+end)//2
    value = 0
    if start > end:
        return
    # mid값과에 차이를 한번에 계산하자. 요소별로 따로 검사하려면 로직이 복잡해짐.
    for level in level_list:
        if mid > level:
            value += (mid-level)

    if value <= k:
        result = max(mid, result)
        return binary_level(mid+1, end)
    else:
        return binary_level(start, mid-1)



result = 0
n, k = map(int,input().split())
level_list = sorted([int(input()) for _ in range(n)])
binary_level(level_list[0],k+level_list[0])
print(result)

