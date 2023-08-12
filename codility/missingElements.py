# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)
    total_sum = (n+1) * (n+2) // 2
    array_sum = sum(A)
    return total_sum - array_sum

print(solution([3,2,1,5]))