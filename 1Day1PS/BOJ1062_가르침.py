import sys
import itertools
input = sys.stdin.readline

#antatica 5개
educated = set(["a", "n", "t", "c", "i"])
n, k = map(int, input().split())
alphabet = k - 5

words = [input().rstrip() for _ in range(n)]
need = 0
total_set = set()
result = []
for word in words:
    word_set = set(word[4:-4]) - educated
    total_set |= word_set

total = list(total_set)
if alphabet < 0 :
    print(0)
    exit()
combinations = itertools.combinations(total, alphabet)
for index, spells in enumerate(combinations):
    result.append(0)
    for spell in spells:
        educated.add(spell)
    for word in words:
        if len(set(word) - educated) == 0:
            result[index] += 1
    educated = set(["a", "n", "t", "c", "i"])
        
print(max(result))