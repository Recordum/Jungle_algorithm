import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(start, node):
    global count

    for i in range(len(node[start])):
        if not visited[node[start][i]]:
            visited[node[start][i]] = True
            count += 1
            dfs(node[start][i], node)

    return


n, m = map(int, input().split())
count = 0
node_light = [[] for _ in range(n+1)]
node_heavy = [[] for _ in range(n+1)]

result = 0
for _ in range(m):
    heavy, light = map(int,input().split())
    node_light[light].append(heavy)
    node_heavy[heavy].append(light)

for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    visited[i] = True
    if node_light[i]:
        dfs(i, node_light)
        if count > n//2:
            result += 1
        count = 0

for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    visited[i] = True
    if node_heavy[i]:
        dfs(i, node_heavy)
        if count > n//2:
            result += 1
        count = 0
print(result)