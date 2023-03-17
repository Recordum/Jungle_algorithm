import sys
input = sys.stdin.readline

v, n = map(int, input().split())
node = [[] for _ in range(v+1)]
result = sys.maxsize
for _ in range(n):
    a, b, c = map(int, input().split())
    node[a].append([b,c])
    node[b].append([a,c])
sum = 0
connect_list = []
for i in range(len(node)):
    if len(node[i]) == v-1:
        connect_list.append(node[i])
        for i in range(len(connect_list[-1])):
            sum += connect_list[-1][i][1]
        result = min(result,sum)
        sum = 0

print(result)

