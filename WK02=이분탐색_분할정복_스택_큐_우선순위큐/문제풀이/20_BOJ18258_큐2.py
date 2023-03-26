import sys
from collections import deque

input = sys.stdin.readline

def queue():
    if instruction[0] == 'push':
        deque_list.append(instruction[1])
        return
    if instruction[0] == 'pop':
        if deque_list:
            return deque_list.popleft()
        return -1
    if instruction[0] == 'size':
        return len(deque_list)
    if instruction[0] == 'empty':
        if deque_list:
            return 0
        return 1
    if instruction[0] == 'front':
        if deque_list:
            return deque_list[0]
        return -1
    if instruction[0] == 'back':
        if deque_list:
            return deque_list[-1]
        return -1

n = int(input())
deque_list = deque([])
answer = []
for _ in range(n):
    instruction = list(input().split())
    result = queue()
    if result != None:
        answer.append(result)

for ans in answer:
    print(ans)