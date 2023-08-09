# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def trans_binary(number):
    return bin(number)[2:]

def solution(N):
    binary_representation = list(map(int,trans_binary(N)))
    max_gap = 0
    count = 0
    for i in range(1, len(binary_representation)):
        if binary_representation[i] == 0:
            count += 1
        if binary_representation[i] == 1 and count > 0:
            max_gap = max(max_gap, count)
            count = 0 
    return max_gap
    # Implement your solution here

print(solution(1042))