import sys
input = sys.stdin.readline

n,p = map(int, input().split())

melody_list = [list(map(int, input().split())) for _ in range(n)]
finger_list = [[] for _ in range(7)]
count = 0
flag = 0

for melody in melody_list:
    while True:
        if len(finger_list[melody[0]]) == 0:
            finger_list[melody[0]].append(melody[1])
            count+=1
            break
        if finger_list[melody[0]][-1] == melody[1]:
            break
        if finger_list[melody[0]][-1] > melody[1]:
            finger_list[melody[0]].pop()
            count += 1
            continue
        if finger_list[melody[0]][-1] < melody[1]:
            finger_list[melody[0]].append(melody[1])
            count += 1
            break

print(count)




