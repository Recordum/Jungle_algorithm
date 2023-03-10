import sys
sys.setrecursionlimit(10**6)

def validate_distance(index,mid,count):
    for j in range(index + 1, len(house_list)):
        if mid <= house_list[j] - house_list[index] :
            count += 1
            return validate_distance(j,mid,count)
    return count

def binary_distance(start,end):
    mid = (start+end) // 2

    if start > end:
        return end

    count = validate_distance(0,mid,1)
    if count >= c:
        return binary_distance(mid +1, end)
    if count < c:
        return binary_distance(start, mid-1)

input = sys.stdin.readline
n,c = map(int, input().split())
house_list = [0]*n
result = 0
for i in range(n):
    house_list[i] = int(input())

house_list.sort()

print(binary_distance(1, house_list[-1]))