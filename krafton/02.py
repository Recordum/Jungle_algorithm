# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    stack = []
    b_stack = []
    for letter in S:
        if letter == 'A':
           while stack:
                if stack[-1] == "B":
                   b_stack.append(stack.pop())     
                else:
                    break                   
        stack.append(letter)
    return len(b_stack)
print(solution("BAAABAB"))
