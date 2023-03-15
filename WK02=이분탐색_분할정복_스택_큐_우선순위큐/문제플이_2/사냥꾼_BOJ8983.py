import sys
input = sys.stdin.readline

def binary_search(start, end, animal_x):
    mid = (start + end)//2
    if start > end:
        if 0 <= start < m and 0<=end <m:
            return min(abs(m_list[start] - animal_x), abs(m_list[end] - animal_x))
        if start < 0 or start >= m:
            return abs(m_list[end] - animal_x)
        if end < 0 or end >= m:
            return abs(m_list[start] - animal_x)

    if m_list[mid] == animal_x:
        return 0
    if m_list[mid] > animal_x:
        return binary_search(start, mid -1, animal_x)
    if m_list[mid] < animal_x:
        return binary_search(mid+1, end, animal_x)

    return
m, n, l = map(int, input().split())
m_list = sorted(list(map(int, input().split())))
animal_list = sorted([list(map(int,input().split())) for i in range(n)])
count = 0
for animal in animal_list:
    x_diff = binary_search(0, m-1, animal_x= animal[0])
    if x_diff + animal[1] <= l:
        count += 1

print(count)