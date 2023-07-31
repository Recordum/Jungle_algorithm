import sys
from collections import deque
input = sys.stdin.readline

def setPrime(n):
    for i in range(2, int(n ** 0.5) ):
        if prime_numbers[i] == True:
            for j in range(2 * i, int(n), i):
                prime_numbers[j] = False
    
def bfs(start):

    queue = deque()
    queue.append([start, 0])
    visited[int(''.join(map(str, start)))] = True

    while(queue):
        node, count = queue.popleft()
        if node == goal:
            return count
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0 :
                    continue
                new_node = node[:]
                new_node[i] = j
                number = int(''.join(map(str, new_node)))
                if prime_numbers[number] and not visited[number]:
                    visited[number] = True
                    queue.append((new_node, count + 1))


t = int(input())
result = []
prime_numbers = [True] * 10000

setPrime(10000)
for _ in range(t):
    visited = [False for i in range(10000)]
    init_password, goal_password = map(str, input().split())
    init = list(map(int, init_password))
    goal = list(map(int, goal_password))
    result.append(bfs(init))

for ans in result:
    print(ans if ans != None else "Impossible")