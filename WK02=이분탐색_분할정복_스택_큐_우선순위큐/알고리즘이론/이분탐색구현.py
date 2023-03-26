import sys
input = sys.stdin.readline


# O(logN)
# 10,000,000 -> O(N)으로 풀어야 1초
# 문제에서 주어진 조건과 mid값과에 차이를 구하는게 핵심
def binary_search(target, start, mid, end):
    if search_list[mid] == target:
        return mid
    if end > start:
        return 1000
    if search_list[mid] > target:
        end = mid - 1
        return binary_search(target, start, (start+end)//2, end)
    else:
        start = mid + 1
        return binary_search(target, start, (start+end)//2, end)
    return


search_list = [1,2,3,4,5,6,7,8,9]
n = int(input())
print(binary_search(n, 0, len(search_list)//2 , len(search_list) - 1))


