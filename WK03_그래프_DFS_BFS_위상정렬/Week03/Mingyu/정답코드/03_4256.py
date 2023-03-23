import sys

input = sys.stdin.readline

def find_postorder(preorder, inorder):
    if not preorder: return
    root = preorder[0]

    root_inorder = 0
    for i in range(len(inorder)):
        if inorder[i] == root:
            root_inorder = i
    if root_inorder == len(inorder) - 1:
        left_preorder = preorder[1:]
        left_inorder = inorder[:root_inorder]
        right_preorder = []
        right_inorder = []
    elif root_inorder == 0:
        left_preorder = []
        left_inorder = []
        right_preorder = preorder[1:]
        right_inorder = inorder[1:]
    else:
        left_inorder = inorder[:root_inorder]
        right_inorder = inorder[root_inorder+1:]
        divide = 0
        for i in range(len(preorder)):
            if preorder[i] in right_inorder:
                divide = i
                break
        left_preorder = preorder[1:divide]
        right_preorder = preorder[divide:]

    find_postorder(left_preorder, left_inorder)
    find_postorder(right_preorder, right_inorder)
    print(root, end=" ")


for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    find_postorder(preorder, inorder)
    print()