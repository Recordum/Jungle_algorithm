import sys
input = sys.stdin.readline

sub = 1e9
result = 0 
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            sum = numbers[i] + numbers[j] + numbers[k]
            if m-sum == 0:
                print(sum)
                exit(0)
            if m - sum < 0 :
                continue
            if sub > m - sum:
                sub = m - sum
                result = sum
print(result)


