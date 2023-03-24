import sys
input = sys.stdin.readline

test_case = int(input())
result = []
for t in range(test_case):
    n = int(input())
    coin_list = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m+1)
    dp[0] = 1
    for coin in coin_list:
        for i in range(coin, m+1):
            dp[i] += dp[i-coin]
    result.append(dp[m])

for ans in result:
    print(ans)