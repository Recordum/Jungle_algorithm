import sys
input = sys.stdin.readline
def middle_band(start,end,mid):
    global result
    bandwidth_x = []
    for i in range(start, end+1):
        x_diff = (point[i][0] - point[mid][0])**2
        if x_diff < result:
            bandwidth_x.append(point[i])
        if bandwidth_x and x_diff >= result:
            break

    bandwidth_sort = sorted(bandwidth_x, key= lambda x : x[1])
    for i in range(len(bandwidth_sort)):
        for j in range(i+1, len(bandwidth_sort)):
            if (bandwidth_sort[i][1] - bandwidth_sort[j][1])**2 < result:
                distance = (bandwidth_sort[i][0] - bandwidth_sort[j][0])**2 + (bandwidth_sort[i][1] - bandwidth_sort[j][1])**2
                result = min(result, distance)
            else :
                break
    return
def divide_point(start, end):
    global result
    mid = (start+end) // 2
    if end - start < 3:
        for i in range(start,end+1):
            for j in range(i+1, end+1):
                distance = (point[i][0] - point[j][0])**2 + (point[i][1] - point[j][1])**2
                result = min(result,distance)
        return

    divide_point(start, mid)
    divide_point(mid+1, end)
    middle_band(start, end, mid)
    return

n = int(input())
point = sorted([list(map(int,input().split())) for _ in range(n)], key= lambda x : (x[0]))
result = 1e9
divide_point(0, len(point)-1)
print(result)

