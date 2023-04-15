import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block_list = list(map(int, input().split()))

result = 0
left = 0
right = 0
for i in range(1, w - 1):
    for j in range(0, i):
        left = max(block_list[j], left)
    for k in range(i+1, len(block_list)):
        right = max(block_list[k], right)
    min_height = min(left, right)
    if block_list[i] < min_height:
        result += min_height - block_list[i]
    left = 0
    right = 0

print(result)