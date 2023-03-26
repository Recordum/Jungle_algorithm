import sys
input = sys.stdin.readline

first_str = input().rstrip()
second_str = input().rstrip()

dp_matrix = [[0] * (len(first_str) + 1) for _ in range(len(second_str) + 1)]

for i in range(1, len(second_str)+1):
    for j in range(1, len(first_str)+1):
        max_dp = max(dp_matrix[i-1][j], dp_matrix[i][j-1])
        if second_str[i-1] == first_str[j-1]:
            dp_matrix[i][j] = dp_matrix[i-1][j-1] + 1
            continue

        if dp_matrix[i][j] < max_dp:
            dp_matrix[i][j] = max_dp



print(dp_matrix[-1][-1])

