import sys
import itertools

input = sys.stdin.readline



n = int(input())
k = int(input())
card_set = set()
deck = [input().rstrip() for _ in range(n)]
for cards in itertools.permutations(deck, k):
    card_set.add(''.join(cards))

print(len(card_set))

