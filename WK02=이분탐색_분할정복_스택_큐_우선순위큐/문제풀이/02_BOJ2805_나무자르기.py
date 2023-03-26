import sys
input = sys.stdin.readline

def binary_cut(start ,end):
    global result
    cut = 0
    mid = (end + start)//2
    if end < start:
        return end
    for i in range(len(tree_list)):
        if tree_list[i] - mid <= 0:
            continue
        cut = cut + tree_list[i] - mid
    if cut > m:
        return binary_cut(mid+1, end)
    if cut < m:
        return binary_cut(start, mid-1)
    if cut == m:
        return mid
    #
    #  while(start<=end):
    #     cut = 0
    #     mid = (end + start)//2
    #     for i in range(len(tree_list)):
    #         if tree_list[i] - mid <= 0:
    #             continue
    #         cut = cut + tree_list[i] - mid
    #     if cut >= m:
    #         start = mid+1
    #     if cut < m:
    #         end = mid-1
    # result = end



n, m = map(int, input().split())
tree_list = sorted(list(map(int, input().split())), reverse=True)
print(binary_cut(1, tree_list[0]))
