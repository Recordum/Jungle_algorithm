import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def is_palindrome(start, end):
    if start == end:
        dp_table[start][end] = 1
    if number_list[start] == number_list[end]:
        if start + 1 < n:
            if start + 1 == end:
                dp_table[start][end] = 1
                return
            if dp_table[start+1][end-1]:
                dp_table[start][end] = 1
                return

n = int(input())
number_list = list(map(int, input().split()))
m = int(input())
question = [list(map(int, input().split())) for _ in range(m)]
dp_table = [[0] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        end = i + j
        if end >= n:
            break
        is_palindrome(j, end)

for start, end in question:
    print(dp_table[start-1][end-1])