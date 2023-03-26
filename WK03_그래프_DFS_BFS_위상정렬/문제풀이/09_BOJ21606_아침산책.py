import sys
input = sys.stdin.readline



def dfs(start):
    global count
    if place_list[start - 1] == '1' and visited[start]:
        count += 1
        return
    visited[start] = True
    for i in node[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

n = int(input())
place_list = input()
count = 0
node = [[] for i in range(n+1)]

while True:
    try:
        a, b = map(int,input().split())
        node[a].append(b)
        node[b].append(a)
    except:
        break

for i in range(1, len(node) + 1):
    if place_list[i-1] == '1':
        visited = [False] * (n+1)
        dfs(i)

print(count)