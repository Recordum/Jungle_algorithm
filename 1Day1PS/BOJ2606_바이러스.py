import sys
input = sys.stdin.readline

def virus_dfs(start):
    global result
    for i in range(len(network[start])):
        if not visited[network[start][i]]:
            visited[network[start][i]] = True
            result += 1
            virus_dfs(network[start][i])

result = 0
n = int(input())
m = int(input())
network = [[] for _ in range(n+1)]
visited = [False] * (n+1) 
visited[1] = True
for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

virus_dfs(1)
print(result)