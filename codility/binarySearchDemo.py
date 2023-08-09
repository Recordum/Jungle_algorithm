# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys
sys.setrecursionlimit(10**6)

def binarySearch(start, end, block_list, count):
    mid = (start + end) // 2

    if start > end:
        return start

    block_sum = 0
    block_count = 0

    for block in block_list:
        if block_sum + block > mid:
            block_sum = block
            block_count += 1
        else:
            block_sum += block

    block_count += 1

    if block_count <= count:
        return binarySearch(start, mid-1, block_list, count)
    else:
        return binarySearch(mid + 1, end, block_list, count)

def solution(K, M, A):
    print(binarySearch(max(A), sum(A), A, K))

solution(3, 5, [2, 1, 5, 1, 2, 2, 2])

