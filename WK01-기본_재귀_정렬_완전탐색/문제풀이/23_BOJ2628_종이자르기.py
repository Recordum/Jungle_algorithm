n,m = map(int, input().split())

t = int(input())

cut = []

for i in range(t):
    direction,val = map(input().split())
    if direction == 0:
        n = 1
    if direction == 1:
        n = max(n-val, val)





