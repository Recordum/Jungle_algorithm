import sys
input = sys.stdin.readline

# 정답
# 중요한건 회의가 끝나는 시간이 가장 빠른순으로 정렬시킨후 그리디하게 풀이
# 끝나는 시간이 같을경우 시작시간이 빠른순서대로 정렬해야함을 유의

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

sorted_time = sorted(time, key=lambda x: (x[1], x[0]))
count = 1
start, end = sorted_time[0]
for i in range(1, len(sorted_time)):
    next_start, next_end = sorted_time[i]
    if next_start >= end:
        start = next_start
        end = next_end
        count += 1 

print(count)