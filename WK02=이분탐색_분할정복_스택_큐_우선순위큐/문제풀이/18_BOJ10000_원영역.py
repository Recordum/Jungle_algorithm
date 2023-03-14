import sys
input = sys.stdin.readline

def point_chain(index, pre_end, origin_end, count):
    if pre_end == origin_end:
        point_stack.pop()
        point_stack.append([sorted_point[index][0], sorted_point[index][1]])
        return count + 1
    for i in range(index, len(sorted_point)):
            if sorted_point[index][1] == origin_end:
                point_stack.pop()
                point_stack.append([sorted_point[index][0], sorted_point[index][1]])
                return count + 2
            if pre_end == sorted_point[index][0] and sorted_point[index][1] < origin_end:
                if index + 1 >= len((sorted_point)):
                    return count
                return point_chain(index+1, sorted_point[index+1][1], origin_end, count+1)
    return count

n = int(input())
circle_list = [list(map(int,input().split())) for i in range(n)]

point_list = []
for circle in circle_list:
    start = circle[0] - circle[1]
    end = circle[0] + circle[1]
    point_list.append([start, end])

sorted_point = sorted(point_list, key= lambda x : (x[0], -x[1]))
flag = False
count = 1
point_stack = [[sorted_point[0][0], sorted_point[0][1]]]
visited = [False for _ in range(n)]
index = 1
for i in range(1, n):
    start = point_stack[0][0]
    end = point_stack[0][1]
    if start <= sorted_point[i][0] and sorted_point[i][1] <= end:
        count  = point_chain(i + 1, sorted_point[i][1],end,1)
    else :
        count += 1

print(count + 1)





