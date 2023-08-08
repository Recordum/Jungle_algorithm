import sys
input = sys.stdin.readline

n = int(input())

timer_list = [300, 60, 10]
timer_count = [0, 0, 0]



for i in range(3):
    if n >= timer_list[i]:
        timer_count[i] += n // timer_list[i]
        n %= timer_list[i]
    if n == 0:
        break    

if not n == 0:
    print(-1)
else:
    print(" ".join(map(str, timer_count)))