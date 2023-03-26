import sys
from itertools import combinations

input = sys.stdin.readline

dwarf_list = [int(input()) for _ in range(9)]
seven_dwarfs = list(combinations(dwarf_list, 7))
for dwarfs in seven_dwarfs:
    if sum(dwarfs) == 100:
        dwarfs = sorted(dwarfs)
        for dwarf in dwarfs:
            print(dwarf)
        break
