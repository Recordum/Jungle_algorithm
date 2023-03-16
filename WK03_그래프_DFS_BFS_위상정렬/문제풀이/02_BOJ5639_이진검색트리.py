import sys
sys.setrecursionlimit(10**9)



def divide_conquer(root_index, end_index):

    if root_index > end_index:
        return
    right_index = end_index + 1
    for i in range(root_index, len(post_node)):
        if post_node[root_index] < post_node[i]:
            right_index = i
            break

    divide_conquer(root_index + 1, right_index -1)
    divide_conquer(right_index, end_index)
    print(post_node[root_index])

post_node = []
while True:
    try:
        post_node.append(int(sys.stdin.readline()))
    except:
        break

divide_conquer(0, len(post_node)-1)