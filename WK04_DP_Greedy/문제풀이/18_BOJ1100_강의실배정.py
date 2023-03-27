import sys
import heapq
input = sys.stdin.readline

n = int(input())
lecture = [list(map(int, input().split())) for _ in range(n)]
lecture.sort()

if not lecture[0][1]:
    print(0)
    exit()
room = []
heapq.heappush(room, lecture[0][1])
for i in range(1,n):
    end_time = heapq.heappop(room)
    if end_time > lecture[i][0]:
        heapq.heappush(room,lecture[i][1])
        heapq.heappush(room, end_time)
    else:
        heapq.heappush(room,lecture[i][1])
print(len(room))

# 8
# 1 8
# 9 16
# 3 7
# 8 10
# 10 14
# 5 6
# 6 11
# 11 12