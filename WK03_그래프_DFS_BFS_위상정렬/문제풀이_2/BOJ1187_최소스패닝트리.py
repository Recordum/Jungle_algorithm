import sys
input = sys.stdin.readline


def find_root(node):
    if node != root_table[node]:
        return find_root(root_table[node])
    return root_table[node]


def mst_kruskal():
    global result
    for edge in edges:
        cost = edge[0]
        start_node = edge[1]
        end_node = edge[2]

        root_start = find_root(start_node)
        root_end = find_root(end_node)
        if root_start != root_end:
            if root_start < root_end:
                root_table[root_end] = root_start
            else :
                root_table[root_start] = root_end
            result += cost
    return


v, e = map(int, input().split())
edges = []
result = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])
edges.sort()
root_table = [i for i in range(v+1)]
mst_kruskal()
print(result)
