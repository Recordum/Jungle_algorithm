import sys
input = sys.stdin.readline

n = int(input())
k= int(input())
sensor_list = list(map(int, input().split()))
sensor_list.sort()
diff = []
for i in range(1, len(sensor_list)):
    differ = sensor_list[i] - sensor_list[i-1]
    diff.append(differ)

diff.sort()

print(sum(diff[:n-k]))