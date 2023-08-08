import sys
input = sys.stdin.readline

n, length = map(int, input().split())
pool_list = []

for _ in range(n):
    start, end = map(int, input().split())
    pool_list.append([start, end])

pool_list.sort()
count = 0 
new_start = 0
for start, end in pool_list:
    if new_start >= end:
        continue
    if new_start > start:
        start = new_start
    count += (end - start) // length
    least = (end - start) % length 
    if not least == 0:
        count += 1
        new_start = end + (length - least)

print(count)

