import sys
input = sys.stdin.readline

# 오답
# DP로 최적값을 구하는 조건은 맞았으나
# 최적값이 불가능한 상황에서 -1을 반환하도록 로직을짜야하는데 그 부분을 놓침
# DP로 최적값을 구하는 방법을 빨리 떠올렸으면 좀 더 빠르게 구현했을듯
# DP 구별법 -> Greedy하게 접근할 문제를 DP테이블에 최적경로를 기록한다고 생각해야함.
n = int(input())
dp = [0] * 5001
dp[3] = 1
dp[5] = 1

for i in range(6, n + 1):
    if dp[i-3]:
        dp[i] = dp[i-3] + 1

    if dp[i-5]:
        if dp[i]:
            dp[i] = min(dp[i], dp[i-5] + 1)
        else:
            dp[i] = dp[i-5] + 1

if dp[n]:
    print(dp[n])
else:
    print(-1)