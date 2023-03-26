import sys
input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()
third = input().rstrip()
reverse_new_str = []
dp_matrix = [[[0]*(len(first) + 1) for _ in range(len(second) + 1)]for _ in range(len(third) + 1)]
for i in range(1, len(third) + 1):
    for j in range(1, len(second) + 1):
        for k in range(1, len(first) + 1):
            max_value = max(dp_matrix[i-1][j][k], dp_matrix[i][j-1][k], dp_matrix[i][j][k-1])
            if second[j-1] == first[k-1] and third[i-1] == second[j-1]:
                dp_matrix[i][j][k] = dp_matrix[i-1][j-1][k-1] + 1
                continue
            if dp_matrix[i][j][k] < max_value:
                dp_matrix[i][j][k] = max_value

print(dp_matrix[-1][-1][-1])