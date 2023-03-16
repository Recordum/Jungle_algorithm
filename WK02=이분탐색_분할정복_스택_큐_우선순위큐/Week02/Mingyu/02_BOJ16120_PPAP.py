import sys
input = sys.stdin.readline


ppaps = input().rstrip()
stack = []


for i in range(len(ppaps)):
    stack.append(ppaps[i])
    if stack[-4:] == ['P', 'P', 'A', 'P']:
        for i in range(4):
            stack.pop()
        stack.append('P')

if stack == ['P', 'P', 'A', 'P'] or stack == ['P']:
    print('PPAP')
else:
    print('NP')