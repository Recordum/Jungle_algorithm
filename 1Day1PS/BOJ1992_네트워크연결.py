import sys

input = sys.stdin.readline

def find_root(node):
    if node != root[node]:
        return find_root(root[node])
    return root[node]

def union_root(node_a, node_b):
    if node_a > node_b:
        root[node_a] = node_b
    else:
        root[node_b] = node_a
    return

def mst():
    global result
    for edge in edges:
        cost, node_a, node_b = edge
        root_a = find_root(node_a) 
        root_b =  find_root(node_b)
        if root_a != root_b:
            union_root(root_a, root_b)
            result += cost
          

result = 0
n = int(input())
m = int(input())
edges = []
root = [i for i in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append([cost, a, b])
edges.sort()
mst()
print(result)