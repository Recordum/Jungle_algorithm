import itertools
import sys

input = sys.stdin.readline

n = int(input())
number_list = [i for i in range(1, n+1)]

for number in itertools.permutations(number_list, n):
    print(" ".join(map(str, number)))
    