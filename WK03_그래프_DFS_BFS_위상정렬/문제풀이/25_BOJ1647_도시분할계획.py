import sys
input = sys.stdin.readline


def find_root(node):
    if node != root[node]:
        return find_root(root[node])
    return root[node]

def mst():
    global result
    global divide_road_cost
    for cost,start,next in edges:

        root_start = find_root(start)
        root_next = find_root(next)

        if root_start != root_next:
            if root_start < root_next:
                root[root_next] = root_start
            else:
                root[root_start] = root_next
            result += cost
            divide_road_cost = max(cost, divide_road_cost)
    return

result = 0
divide_road_cost = 0
n, m, = map(int, input().split())
edges = []
root = [i for i in range(n+1)]
for _ in range(m):
    a, b, cost = map(int,input().split())
    edges.append([cost, a, b])
edges.sort()
mst()
print(result - divide_road_cost)