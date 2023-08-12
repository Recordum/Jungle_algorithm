# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    count = 0
    count += (Y - X) // D  
    if not (Y - X) % D == 0:
        count += 1
    return count

print(solution(10, 85, 30))
