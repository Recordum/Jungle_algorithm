import sys
import itertools

input = sys.stdin.readline
n, m = map(int,input().split())
deck_list = list(map(int, input().split()))
black = 0
for cards in itertools.combinations(deck_list, 3):
    if sum(cards) < m:
        black = max(sum(cards),black)
    elif sum(cards) == m:
        black = sum(cards)
        print(black)
        exit()

print(black)
