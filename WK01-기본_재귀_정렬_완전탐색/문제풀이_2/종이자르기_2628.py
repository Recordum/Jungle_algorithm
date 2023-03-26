import sys
input = sys.stdin.readline

c, r = map(int, input().split())
n = int(input())

vertical = [r,0]
horizontal = [c,0]
for i in range(n):
    direction, value = map(int,input().split())
    if direction == 0:
        vertical.append(value)
        continue
    horizontal.append(value)

vertical.sort()
horizontal.sort()

cut_row = [vertical[i] - vertical[i-1] for i in range(1,len(vertical))]
cut_col = [horizontal[i] - horizontal[i-1] for i in range(1,len(horizontal))]

print(max(cut_row) * max(cut_col))

