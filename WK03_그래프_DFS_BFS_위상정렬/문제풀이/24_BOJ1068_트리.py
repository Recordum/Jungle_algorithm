import sys
input = sys.stdin.readline


def dfs(start):
    global count
    flag = 0
    if visited[start]:
        return
    if not len(graph[start]):
        count += 1
        return
    for i in range(len(graph[start])):
        if not visited[graph[start][i]]:
            dfs(graph[start][i])
        else:
            flag += 1
            if flag == len(graph[start]):
                count += 1
                flag = 0
    return

count = 0
n = int(input())
node = list(map(int, input().split()))
delete_node = int(input())

graph = [[] for _ in range(n)]
start = 0
for i in range(len(node)):
    if node[i] == -1:
        start = i
    else:
        graph[node[i]].append(i)

visited = [False] * n
visited[delete_node] = True
dfs(start)
print(count)