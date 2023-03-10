import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def binary_search(start, end, x_index):
    mid = (start+end)//2
    if locate_list[x_index] == m_list[mid]:
        return mid

    if start >= end:
        return end

    if locate_list[x_index][0] > m_list[mid]:
        return binary_search(mid + 1, end, x_index)
    if locate_list[x_index][0] < m_list[mid]:
        return binary_search(start, mid-1, x_index)

    return end


m,n,l = map(int, input().split())
m_list = sorted(list(map(int,input().split())))
locate_list = [list(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(len(locate_list)):
    if len(m_list) == 1:
        x_diff = abs(locate_list[i][0] - m_list[0])
    else :
        end = binary_search(0, len(m_list)-1, i)
    if abs(m_list[end]-locate_list[i][0])+locate_list[i][1]<=l or abs(m_list[end-1]-locate_list[i][0])+locate_list[i][1]<=l:
        count += 1
print(count)