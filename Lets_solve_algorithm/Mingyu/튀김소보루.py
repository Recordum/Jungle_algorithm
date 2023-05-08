import sys
input = sys.stdin.readline

n, s = map(int, input().split())
# 정답
m = int(input())
people = [int(input()) for _ in range(m)]
current_time = 0
count = 0

while True:
    for i in range(len(people)):
        if current_time % people[i] == 0:
            count += 1
            if count >= (n-s):
                print(i+1)
                exit(0)
    current_time += 1
