# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque
def circular_array(array, shift_count):
    if len(array) == 0 :
        return []
    que = deque(array)
    for _ in range(shift_count):
        que.appendleft(que.pop())
    return que

def solution(A, K):
    return circular_array(A,K)

print(solution([3,8,9,7,6], 3))