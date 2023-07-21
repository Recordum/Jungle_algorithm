import sys
import itertools

input = sys.stdin.readline
results = []
index = 0
while True:
    number_list = list(map(int, input().split()))
    if number_list[0] == 0:
        break
    lotto_number_list = number_list[1:]
    combinations = list(itertools.combinations(lotto_number_list, 6))
    results.append(combinations)
    index += 1

for result in results:
    for lotto in result:
        print(" ".join(map(str, lotto)))
    print(" ")
