import sys
input = sys.stdin.readline


def is_prime_number(n):
    for i in range(2,int(n**(0.5)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
result = [""] * t
for case in range(t):
    n = int(input())
    for i in range(int(n/2)):
        if is_prime_number(int(n/2) + i) and is_prime_number(int(n/2) - i):
            result[case] = str(int(n/2) - i) + " " + str(int(n/2) + i)
            break

for case in range(t):
    print(result[case])

