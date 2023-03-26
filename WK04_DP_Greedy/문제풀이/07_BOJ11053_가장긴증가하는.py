import sys
input = sys.stdin.readline

n = int(input())
sequence_list = list(map(int, input().split()))
dp = [0] * len(sequence_list)
for i in range(len(sequence_list)):
    dp[i] = 1
    for j in range(0, i + 1):
        if sequence_list[j] < sequence_list[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
