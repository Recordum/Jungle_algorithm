import sys
input = sys.stdin.readline

def divide_plane(start, end):
    global result


result = 1e9
n= int(input())

coordinate_list = sorted([list(map(int, input().split())) for i in range(n)])

print(result)
