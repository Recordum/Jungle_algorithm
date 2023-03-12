import sys
input = sys.stdin.readline

n = int(input())

height_list = [int(input()) for i in range(n)]
current_height = height_list[-1]
count = 1
for i in range(len(height_list)-2, -1,-1):
    if current_height < height_list[i]:
         current_height = height_list[i]
         count += 1

print(count)