import sys
input = sys.stdin.readline

def find_root(node):
    if node != root[node]:
        root[node] = find_root(root[node])
    return root[node]

def mst_kruskal():
    global result
    for edge in edges:
        cost, node_a, node_b = edge
        root_a = find_root(node_a)
        root_b = find_root(node_b)
        if root_a != root_b:
            if root_a < root_b:
                root[root_b] = root_a
            else :
                root[root_a] = root_b
            result += cost
    return

result = 0
v, n = map(int, input().split())
edges= []
root = [i for i in range(v+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])
edges.sort()
mst_kruskal()
print(result)

