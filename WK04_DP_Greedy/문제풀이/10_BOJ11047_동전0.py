import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
count = 0
for i in range(1, len(coin_list) + 2):
    if k // coin_list[-i] > 0:
        count += k // coin_list[-i]
        k -= (k // coin_list[-i]) * coin_list[-i]
    if k == 0:
        break
print(count)
