import sys
import heapq
input = sys.stdin.readline
nominate = []

n = int(input())
m = int(input())
recommend = list(map(int, input().split()))
flag = 0

for r in recommend:
    if len(nominate) >= n:
        for i in range(len(nominate)):
            if nominate[i][1] == r:
                nominate[i][0] += 1
                flag = 1
                break
        if flag == 0:
            nominate_sorted = sorted(nominate, key = lambda x : x[1])

            heapq.heapify(nominate)
            heapq.heappush(nominate, [0, r])
    else:
        for i in range(len(nominate)):
            if nominate[i][1] == r:
                nominate[i][0] += 1
                flag = 1
                break
        if flag == 0:
            heapq.heappush(nominate, [0, r])
    flag = 0

nominate_sorted = sorted(nominate, key = lambda x : x[1])
for i in range(len(nominate)):
    count, student = heapq.heappop(nominate_sorted)
    print(str(student) + " " ,end="")
