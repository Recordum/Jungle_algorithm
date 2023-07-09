import sys
input = sys.stdin.readline

n = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))
dp = [0] * 101
for i in range(n):
    cost_hp = hp[i]
    take_happy = happy[i]
    for j in range(1, 101)[::-1]:
        if j - cost_hp > 0:
            dp[j] = max(dp[j], dp[j - cost_hp] + take_happy)

print(dp[-1])