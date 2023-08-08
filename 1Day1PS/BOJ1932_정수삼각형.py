import sys
input = sys.stdin.readline

n = int(input())

tree= [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(n-1, 0, -1):
    for j in range(len(tree[i]) -1):
        tree[i-1][j] = max(tree[i-1][j] + tree[i][j], tree[i-1][j] + tree[i][j+1])

print(tree[0][0])
