import sys
input = sys.stdin.readline

def preorder_traversal(start):
    result[0].append(start)
    if tree_dict[start][0] == '.' and tree_dict[start][1] == '.':
        result[2].append(start)
        if not start in result[1]:
            result[1].append(start)
        return
    if not tree_dict[start][0] == ".":
        preorder_traversal(tree_dict[start][0])
        if not start in result[1]:
            result[1].append(start)
    if not tree_dict[start][1] == ".":
        if not start in result[1]:
            result[1].append(start)
        preorder_traversal(tree_dict[start][1])
    result[2].append(start)
    return
# result[0] preorder
# result[1] inorder
# result[2] postorder
n = int(input())
tree_dict = dict()
result = [[] for _ in range(3)]
visited = dict()
start = 'A'
for _ in range(n):
    parent, left_child, right_child = map(str, input().split())
    visited[parent] = False
    tree_dict[parent] = [left_child, right_child]
preorder_traversal(start)
# inorder_traversal(start)
# postorder_traversal(start)
for ans in result:
    print("".join(ans))