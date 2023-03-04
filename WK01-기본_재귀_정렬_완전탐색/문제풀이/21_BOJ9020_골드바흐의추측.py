import sys
# input = sys.stdin.readline().rstrip()
results = []

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2,x):
        if int(x % i) == 0:
            return False

    return True

results = []
t = int(input())
for i in range(t):
    n = int(input())
    x = int(n / 2)
    y = int(n / 2)
    while(x > 0):
        if is_prime_number(x) and is_prime_number(y):
           results.append(list([x, y]))
           break

        x = x - 1
        y = y + 1

for result in results:
    print(str(result[0]) +" "+ str(result[1]))






