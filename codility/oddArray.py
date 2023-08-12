# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    array = A
    duplication_checker = set()
    
    while array:
        element = array.pop()
        if element in duplication_checker:
            duplication_checker.remove(element)
        else:
            duplication_checker.add(element)

    return duplication_checker.pop()


print(solution([9, 3, 9, 3, 9, 7, 9]))