# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    stack = []
    for letter in S:
        if not stack:
            stack.append(letter)
            continue
        if letter == "A" and stack[-1] == "B":
            stack.pop()
            continue
        if letter == "B" and stack[-1] == "A":
            stack.pop()
            continue
        if letter == "C" and stack[-1] == "D":
            stack.pop()
            continue
        if letter == "D" and stack[-1] == "C":
            stack.pop()
            continue
        stack.append(letter)
    
    return "".join(stack)

print(solution("CBACD"))
