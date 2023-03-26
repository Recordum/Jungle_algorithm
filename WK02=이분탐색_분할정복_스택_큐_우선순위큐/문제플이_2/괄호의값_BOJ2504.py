import sys
input = sys.stdin.readline

def count_number():
    stack = []
    temp = 1
    count = 0

    for index, par in enumerate(parenthesis):
        if par == "(":
            stack.append(parenthesis[index])
            temp *= 2
        elif par == "[":
            stack.append(parenthesis[index])
            temp *= 3
        elif par == ")":
            if not stack or stack[-1] == "[":
                return 0
            if parenthesis[index-1] == "(":
                count += temp
            stack.pop()
            temp //= 2
        else:
            if not stack or stack[-1] == "(":
                return 0
            if parenthesis[index-1] == "[":
                count += temp
            stack.pop()
            temp //= 3
    if stack:
        return 0
    return count


parenthesis = input().rstrip()
print(count_number())
