import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(start, count):
    global result_road
    global result_time
    if start == end:
        if result_time <= count:
            if result_time != count:
                result_road.clear()
            result_time = count
            result_road = set(temp_road)
        return
    for i in range(len(node[start])):
        next, distance = node[start][i]
        temp_road.append((start, next))
        dfs(next, count + distance)
        temp_road.pop()
    return

n = int(input())
m = int(input())
node = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, dis = map(int,input().split())
    node[a].append([b,dis])
result_time = 0
result_road = set()
temp_road = []
start, end = map(int,input().split())
dfs(start, 0)
print(result_time)
print(len(result_road))

