import sys
input = sys.stdin.readline


def binary_search(target, start, mid, end):
    if n_list[mid] == target or n_list[start] == target or n_list[end] == target:
        return 1
    if end <= start:
        return 0

    if target > n_list[mid]:
        start = mid + 1
        return binary_search(target, mid+1, (start+end)//2, end)
    if target < n_list[mid]:
        end = mid -1
        return binary_search(target, start, (start+end)//2, mid-1)

n = int(input())
n_list = sorted(list(map(int,input().split())))
m = int(input())
m_list = list(map(int, input().split()))
result = [0]*m

for i in range(len(m_list)):
    result[i] = binary_search(m_list[i], 0, (n-1)//2, n-1)
for i in range(m):
    print(result[i])
