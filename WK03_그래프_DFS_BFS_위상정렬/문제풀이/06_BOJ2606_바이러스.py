import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    global count
    visited[start] = True

    for i in range(len(node[start])):
        if not visited[node[start][i]]:
            visited[node[start][i]] = True
            count += 1
            dfs(node[start][i])
    return

n = int(input())
m = int(input())
visited = [False for _ in range(n+1)]
node = [[] for _ in range(n+1)]
count = 0
for _ in range(m):
    a, b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

dfs(1)
print(count)