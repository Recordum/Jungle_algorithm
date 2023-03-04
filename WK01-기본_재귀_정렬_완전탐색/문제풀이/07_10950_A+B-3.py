n = int(input())
result = [0] * n
for i in range(n):
   m, k = map(int, input().split())
   result[i] = m + k

for i in range(len(result)):
    print(result[i])