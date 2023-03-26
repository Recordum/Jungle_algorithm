import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def find_parent(start):
    visited[start] = True

    for i in range(len(node[start])):
        if not visited[node[start][i]]:
            find_parent(node[start][i])
            parent_node[node[start][i]] = start
    return

n =int(input())
parent_node = [0 for i in range(n+1)]
node = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
while True:
    try:
        a ,b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    except:
        break
find_parent(1)
for i in range(2, len(parent_node)):
    print(parent_node[i])