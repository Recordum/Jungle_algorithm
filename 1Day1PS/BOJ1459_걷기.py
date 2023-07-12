import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())

mov_normal = (x+y) * w

if x >= y:
    mov_diag = x*s
    mov = (x - y) * w + (x - y) * s
else:
    mov_diag = y*s
    mov = (y - x) * w + (y - x) * s

res = min(mov_normal, mov_diag, mov)
print(mov_diag)
print(mov)
print(mov_normal)
print(res)
