import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global result
    q = deque([])
    q.append([n, 0])
    visited[n] = True
    while q:
        location, count = q.popleft()
        if location == k:
            result = min(result,count)
            return
        for i in range(len(move)):
            if not location + move[i] < 0 and not location + move[i] > 100000:
                if not visited[location + move[i]]:
                    new_loc = location + move[i]
                    visited[location + move[i]] = True
                    q.append([new_loc, count +1])

        jump_loc = location * jump
        if not jump_loc < 0 and not jump_loc > 100000:
            visited[jump_loc] = True
            q.append([jump_loc, count + 1])
    return

result = 1e9
move = [-1, 1]
jump = 2
n, k = map(int, input().split())
visited = [False] * 100001
bfs()
print(result)