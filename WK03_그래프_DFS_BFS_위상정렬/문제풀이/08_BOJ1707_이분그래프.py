import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 노드가 서로 연결되지 않는 부분들이 존재함을 유의해야함
def dfs(start, pre_flag):
    global result_flag
    if flag[start] == pre_flag:
        result_flag = False
        return
    if visited[start]:
        return
    visited[start] = True
    for i in range(len(node[start])):
        if not visited[node[start][i]]:
            if flag[start]:
                flag[node[start][i]] = False
            else:
                flag[node[start][i]] = True
        dfs(node[start][i], flag[start])
    return


test_case = int(input())
result = [[] for _ in range(test_case)]
for t in range(test_case):
    result_flag = True
    v, e, = map(int, input().split())
    node = [[] for _ in range(v+1)]
    flag = [''] * (v+1)
    visited = [False] * (v+1)
    root = [i for i in range(v+1)]
    for _ in range(e):
        a, b = map(int,input().split())
        node[a].append(b)
        node[b].append(a)
    for i in range(1, len(node)):
        if not visited[i]:
            flag[i] = True
            dfs(i,False)
    if result_flag:
        result[t] = 'YES'
    else:
        result[t] = 'NO'

for ans in result:
    print(ans)

