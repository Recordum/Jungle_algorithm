import sys
T = int(input())

def postorder(preorder, inorder):
    if not preorder:
        return

    # inorder에서의 루트의 인덱스
    in_root = inorder.index(preorder[0])

    # 오른쪽 시작 인덱스 (pre/inorder 둘 다 오른쪽 시작은 동일)
    right = in_root +1

    # 왼쪽 -> pre: 루트 뒤~ 오른쪽 전까지, in: 루트 전까지
    postorder(preorder[1:right], inorder[:in_root])

    # 오른쪽 ->  pre: 오른쪽 ~ 끝까지, in: 오른쪽 ~ 끝까지
    postorder(preorder[right:], inorder[right:])

    # 루트 출력
    print(inorder[in_root])


for _ in range(T):
    N = int(input())
    preorder = list(map(int,sys.stdin.readline().split()))
    inorder = list(map(int,sys.stdin.readline().split()))
    postorder(preorder, inorder)