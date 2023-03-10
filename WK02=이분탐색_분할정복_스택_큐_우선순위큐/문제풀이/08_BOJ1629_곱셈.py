import sys
input = sys.stdin.readline

def divide_exp(a, b):
    if b == 1:
        return a % c

    half_value = divide_exp(a, b // 2)

    if b % 2 == 0:
        return half_value * half_value % c
    else:
        return half_value * half_value * a % c


a, b, c = map(int,input().split())
print(divide_exp(a,b) % c)