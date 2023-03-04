
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2,x):
        if int(x % i) == 0:
            return False

    return True

t = int(input())
count = 0
arrays = list(map(int, input().split()))
for array in arrays:
    if is_prime_number(array):
        count += 1

print(count)
